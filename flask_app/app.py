"""
Perinatal Mental Health Screening Application
Flask Web Application
"""

from flask import Flask, render_template, request, jsonify, session, redirect, url_for, flash
from datetime import datetime
import json
import os
from pathlib import Path
from baseline_data import merge_with_new_responses
from database import (
    init_db, create_user, verify_password, update_last_login,
    save_screening_response, get_user_screening_history,
    get_latest_screening, get_all_screening_responses,
    get_user_by_id, get_user_stats
)
from functools import wraps

app = Flask(__name__)
app.secret_key = 'your-secret-key-change-in-production-use-random-string'  # Change this!

# Initialize database
init_db()

# Load questions configuration
config_path = Path(__file__).parent.parent / 'questions_config.json'
with open(config_path, 'r') as f:
    QUESTIONS_CONFIG = json.load(f)


# ============================================================================
# AUTHENTICATION DECORATOR
# ============================================================================

def login_required(f):
    """Decorator to require login for routes"""
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if 'user_id' not in session:
            flash('Please log in to access this page.', 'warning')
            return redirect(url_for('login'))
        return f(*args, **kwargs)
    return decorated_function


# ============================================================================
# HELPER FUNCTIONS
# ============================================================================

def get_all_questions():
    """Get all questions from config in order"""
    questions = []
    for section in QUESTIONS_CONFIG['sections']:
        for question in section['questions']:
            question['section_name'] = section['section_name']
            questions.append(question)
    return questions


def calculate_risk(responses):
    """Calculate risk classification based on responses"""

    # Component 1: PHQ-2 Score
    phq2_q1 = int(responses.get('PHQ2_Q1', 0)) if responses.get('PHQ2_Q1') not in ['NA', None, ''] else 0
    phq2_q2 = int(responses.get('PHQ2_Q2', 0)) if responses.get('PHQ2_Q2') not in ['NA', None, ''] else 0
    phq2_total = phq2_q1 + phq2_q2

    # Component 2: High-Risk Flags
    flag_prior_mh = responses.get('BPG_MH') == '2'
    flag_mh_meds = (responses.get('PRE_RX') == '2' and
                    responses.get('PRE_RX_MH') in ['Yes', 'Not sure'])
    flag_poor_health = responses.get('HTH_GEN') in ['4', '5']

    high_risk_flags = sum([flag_prior_mh, flag_mh_meds, flag_poor_health])

    # Component 3: Lifestyle Risk Score
    lifestyle_risk = 0
    if responses.get('PRE_EXER') == '1':  # No exercise
        lifestyle_risk += 1
    if responses.get('PRE_DIET') == '2':  # Dieting
        lifestyle_risk += 1
    if responses.get('OWGT_OBS') == '2':  # Overweight/obese
        lifestyle_risk += 1

    # Apply Classification Rules
    classification = 'LOW_RISK'
    reason = 'No high-risk criteria met'
    rule_triggered = None

    # Rule 1: Positive PHQ-2 (≥3)
    if phq2_total >= 3:
        classification = 'HIGH_RISK'
        reason = f'Your depression screening score ({phq2_total}/6) suggests you may be experiencing symptoms of depression'
        rule_triggered = 'RULE_1_POSITIVE_PHQ2'

    # Rule 2: Any High-Risk Flag
    elif high_risk_flags >= 1:
        classification = 'HIGH_RISK'
        flag_reasons = []
        if flag_prior_mh:
            flag_reasons.append('prior mental health treatment')
        if flag_mh_meds:
            flag_reasons.append('medications for mood/anxiety')
        if flag_poor_health:
            flag_reasons.append('fair or poor general health')

        reason = f"You reported {', '.join(flag_reasons)} which are important risk factors for perinatal depression"
        rule_triggered = 'RULE_2_HIGH_RISK_FLAG'

    # Rule 3: Borderline symptoms + Multiple lifestyle risks
    elif phq2_total == 2 and lifestyle_risk >= 2:
        classification = 'HIGH_RISK'
        reason = f'Combination of borderline depression symptoms (PHQ-2 score: 2) and {lifestyle_risk} lifestyle risk factors'
        rule_triggered = 'RULE_3_BORDERLINE_LIFESTYLE'

    return {
        'classification': classification,
        'reason': reason,
        'rule_triggered': rule_triggered,
        'phq2_total': phq2_total,
        'high_risk_flags': high_risk_flags,
        'lifestyle_risk': lifestyle_risk,
        'flags': {
            'prior_mh': flag_prior_mh,
            'mh_meds': flag_mh_meds,
            'poor_health': flag_poor_health
        }
    }


def determine_routing(bpg_talk, flu_src):
    """Determine care routing based on responses"""

    existing_provider = bpg_talk == '2'

    care_settings = {
        '1': {
            'name': 'OB/Gyn office',
            'referral': 'Contact an OB/Gyn office that has integrated behavioral health services. Many OB/Gyn practices now offer mental health screening and support as part of routine prenatal care.'
        },
        '2': {
            'name': 'Family doctor / Primary care physician',
            'referral': 'Your family doctor can treat perinatal depression or refer you to specialists. Primary care physicians often have behavioral health consultants in their practice.'
        },
        '3': {
            'name': 'Community health clinic',
            'referral': 'Community health clinics often provide integrated mental health and prenatal care services, often on a sliding scale based on income. Federally Qualified Health Centers (FQHCs) serve all patients regardless of insurance.'
        },
        '4': {
            'name': 'Hospital',
            'referral': 'Hospital systems often have specialized perinatal psychiatry programs. Contact the hospital\'s maternal mental health program or OB/Gyn behavioral health services.'
        },
        '5': {
            'name': 'Pharmacy',
            'referral': 'For mental health support during pregnancy, we recommend telehealth services with perinatal specialists. Platforms like Talkspace, BetterHelp, and Maven Clinic offer same-day appointments.'
        },
        '6': {
            'name': 'Work or school clinic',
            'referral': 'Check your Employee Assistance Program (EAP) for free therapy sessions (typically 3-8 sessions). If you\'re a student, your campus health services likely offer free or low-cost counseling.'
        },
        '7': {
            'name': 'Other',
            'referral': 'We recommend telehealth mental health services for quick access to perinatal specialists. Many platforms offer same-day video appointments.'
        }
    }

    setting = care_settings.get(flu_src, {
        'name': 'No regular provider',
        'referral': 'We recommend connecting with telehealth mental health services or visiting a community health clinic. Many resources are available regardless of insurance status.'
    })

    return {
        'existing_provider': existing_provider,
        'setting_name': setting['name'],
        'referral_text': setting['referral']
    }


# ============================================================================
# AUTHENTICATION ROUTES
# ============================================================================

@app.route('/register', methods=['GET', 'POST'])
def register():
    """User registration"""
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')
        confirm_password = request.form.get('confirm_password')
        first_name = request.form.get('first_name')
        last_name = request.form.get('last_name')

        # Validation
        if not email or not password:
            flash('Email and password are required.', 'danger')
            return redirect(url_for('register'))

        if password != confirm_password:
            flash('Passwords do not match.', 'danger')
            return redirect(url_for('register'))

        if len(password) < 6:
            flash('Password must be at least 6 characters.', 'danger')
            return redirect(url_for('register'))

        # Create user
        user_id = create_user(email, password, first_name, last_name)

        if user_id:
            flash('Account created successfully! Please log in.', 'success')
            return redirect(url_for('login'))
        else:
            flash('Email already exists. Please log in.', 'warning')
            return redirect(url_for('login'))

    return render_template('register.html')


@app.route('/login', methods=['GET', 'POST'])
def login():
    """User login"""
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')

        user = verify_password(email, password)

        if user:
            session['user_id'] = user['id']
            session['user_email'] = user['email']
            session['user_name'] = user['first_name'] or email.split('@')[0]
            update_last_login(user['id'])
            flash(f'Welcome back, {session["user_name"]}!', 'success')
            return redirect(url_for('index'))
        else:
            flash('Invalid email or password.', 'danger')
            return redirect(url_for('login'))

    return render_template('login.html')


@app.route('/logout')
def logout():
    """User logout"""
    session.clear()
    flash('You have been logged out.', 'info')
    return redirect(url_for('index'))


@app.route('/profile')
@login_required
def profile():
    """User profile page"""
    user = get_user_by_id(session['user_id'])
    stats = get_user_stats(session['user_id'])
    history = get_user_screening_history(session['user_id'])

    return render_template('profile.html', user=user, stats=stats, history=history)


# ============================================================================
# MAIN ROUTES
# ============================================================================

@app.route('/')
def index():
    """Home page"""
    return render_template('index.html')


@app.route('/screening')
@login_required
def screening():
    """Screening questionnaire page"""
    questions = get_all_questions()
    return render_template('screening.html', questions=questions)


@app.route('/api/questions')
def api_questions():
    """API endpoint to get all questions"""
    questions = get_all_questions()
    return jsonify(questions)


@app.route('/api/submit', methods=['POST'])
@login_required
def api_submit():
    """API endpoint to submit responses and calculate risk"""
    data = request.json
    responses = data.get('responses', {})

    # Calculate risk
    risk_result = calculate_risk(responses)

    # Determine routing
    routing = determine_routing(
        responses.get('BPG_TALK'),
        responses.get('FLU_SRC')
    )

    # Save to database
    user_id = session.get('user_id')
    response_id = save_screening_response(user_id, responses, risk_result, routing)

    # Store in session for results page
    session['last_result'] = {
        'id': response_id,
        'timestamp': datetime.now().isoformat(),
        'responses': responses,
        'risk_result': risk_result,
        'routing': routing
    }

    return jsonify({
        'success': True,
        'risk_result': risk_result,
        'routing': routing
    })


@app.route('/results')
def results():
    """Results page"""
    result = session.get('last_result')
    if not result:
        return redirect('/')

    return render_template('results.html',
                         risk_result=result['risk_result'],
                         routing=result['routing'])


@app.route('/dashboard')
def dashboard():
    """Analytics dashboard"""
    return render_template('dashboard.html')


@app.route('/api/analytics')
def api_analytics():
    """API endpoint for dashboard analytics - includes PRAMS baseline + new responses"""

    # Get all screening responses from database
    all_responses = get_all_screening_responses()

    # Merge baseline PRAMS data with new responses
    analytics = merge_with_new_responses(all_responses)

    return jsonify(analytics)


@app.route('/resources')
def resources():
    """Resources page"""
    crisis_resources = QUESTIONS_CONFIG.get('crisis_resources', {})
    return render_template('resources.html', crisis_resources=crisis_resources)


# ============================================================================
# RUN APP
# ============================================================================

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5001)
