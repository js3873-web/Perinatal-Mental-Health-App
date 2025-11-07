"""
Perinatal Mental Health Screening Application
Flask Web Application
"""

from flask import Flask, render_template, request, jsonify, session, redirect
from datetime import datetime
import json
import os
from pathlib import Path

app = Flask(__name__)
app.secret_key = 'your-secret-key-change-in-production'  # Change this in production!

# Load questions configuration
config_path = Path(__file__).parent.parent / 'questions_config.json'
with open(config_path, 'r') as f:
    QUESTIONS_CONFIG = json.load(f)

# Store responses in memory (in production, use a database)
responses_db = []


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
# ROUTES
# ============================================================================

@app.route('/')
def index():
    """Home page"""
    return render_template('index.html')


@app.route('/screening')
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

    # Store response (with timestamp)
    response_record = {
        'timestamp': datetime.now().isoformat(),
        'responses': responses,
        'risk_result': risk_result,
        'routing': routing
    }
    responses_db.append(response_record)

    # Store in session for results page
    session['last_result'] = response_record

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
    """API endpoint for dashboard analytics"""

    if not responses_db:
        return jsonify({
            'total_responses': 0,
            'risk_distribution': {},
            'phq2_distribution': {},
            'risk_factors': {},
            'care_settings': {}
        })

    # Calculate analytics
    total = len(responses_db)

    # Risk distribution
    risk_dist = {'HIGH_RISK': 0, 'LOW_RISK': 0}
    for record in responses_db:
        risk_dist[record['risk_result']['classification']] += 1

    # PHQ-2 distribution
    phq2_dist = {}
    for record in responses_db:
        score = record['risk_result']['phq2_total']
        phq2_dist[score] = phq2_dist.get(score, 0) + 1

    # Risk factors prevalence
    risk_factors = {
        'prior_mh': 0,
        'mh_meds': 0,
        'poor_health': 0,
        'no_exercise': 0,
        'dieting': 0,
        'overweight': 0
    }

    for record in responses_db:
        responses = record['responses']
        if responses.get('BPG_MH') == '2':
            risk_factors['prior_mh'] += 1
        if responses.get('PRE_RX') == '2' and responses.get('PRE_RX_MH') in ['Yes', 'Not sure']:
            risk_factors['mh_meds'] += 1
        if responses.get('HTH_GEN') in ['4', '5']:
            risk_factors['poor_health'] += 1
        if responses.get('PRE_EXER') == '1':
            risk_factors['no_exercise'] += 1
        if responses.get('PRE_DIET') == '2':
            risk_factors['dieting'] += 1
        if responses.get('OWGT_OBS') == '2':
            risk_factors['overweight'] += 1

    # Care settings
    care_settings_dist = {}
    for record in responses_db:
        setting = record['routing']['setting_name']
        care_settings_dist[setting] = care_settings_dist.get(setting, 0) + 1

    return jsonify({
        'total_responses': total,
        'risk_distribution': risk_dist,
        'phq2_distribution': phq2_dist,
        'risk_factors': risk_factors,
        'care_settings': care_settings_dist
    })


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
