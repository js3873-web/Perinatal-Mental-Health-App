# Perinatal Mental Health Screening - Flask Web Application

A beautiful, modern web application for perinatal mental health screening built with Flask and vanilla JavaScript.

## Features

- **Interactive Screening Questionnaire**: 10-question assessment with conditional logic and progress tracking
- **Risk Classification Algorithm**: Binary classification (Low Risk vs High Risk) based on PHQ-2 and PRAMS data
- **Personalized Results**: Tailored recommendations based on care setting and risk level
- **Analytics Dashboard**: Beautiful data visualizations with Chart.js
- **Crisis Resources**: 24/7 hotlines prominently displayed throughout the app
- **Responsive Design**: Works beautifully on desktop, tablet, and mobile devices
- **Modern UI/UX**: Clean, professional design with smooth animations

## Technology Stack

- **Backend**: Flask (Python)
- **Frontend**: HTML5, CSS3, Vanilla JavaScript
- **Charts**: Chart.js
- **Icons**: Font Awesome
- **Fonts**: Google Fonts (Inter)

## Project Structure

```
flask_app/
├── app.py                      # Main Flask application
├── requirements.txt            # Python dependencies
├── README.md                   # This file
├── templates/                  # HTML templates
│   ├── base.html              # Base template with navigation
│   ├── index.html             # Home page
│   ├── screening.html         # Screening questionnaire
│   ├── results.html           # Results page
│   ├── dashboard.html         # Analytics dashboard
│   └── resources.html         # Crisis resources page
├── static/                     # Static assets
│   ├── css/
│   │   └── style.css          # Main stylesheet
│   └── js/
│       ├── screening.js       # Questionnaire functionality
│       └── dashboard.js       # Dashboard charts
└── data/                       # Data storage (optional)
```

## Installation

### Prerequisites

- Python 3.8 or higher
- pip (Python package manager)

### Setup Steps

1. **Navigate to the flask_app directory**:
   ```bash
   cd flask_app
   ```

2. **Create a virtual environment** (recommended):
   ```bash
   python3 -m venv venv
   ```

3. **Activate the virtual environment**:
   - On macOS/Linux:
     ```bash
     source venv/bin/activate
     ```
   - On Windows:
     ```bash
     venv\Scripts\activate
     ```

4. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

5. **Run the application**:
   ```bash
   python app.py
   ```

6. **Open your browser** and navigate to:
   ```
   http://localhost:5000
   ```

## Usage

### For Users

1. **Home Page**: Learn about the screening and click "Start Screening"
2. **Screening**: Answer 10 questions about your mental health, lifestyle, and healthcare access
3. **Results**: View your risk classification with personalized recommendations
4. **Dashboard**: See aggregate analytics from all responses (for administrators)
5. **Resources**: Access 24/7 crisis hotlines and additional support

### For Developers

#### Modifying Questions

Questions are loaded from `../questions_config.json`. To modify questions:

1. Edit the JSON configuration file
2. Restart the Flask application
3. Changes will be reflected immediately

#### Customizing Styling

- Edit `static/css/style.css` to customize colors, fonts, and layout
- CSS variables at the top of the file make it easy to change the color scheme

#### Adding Database Support

The current implementation stores responses in memory. For production:

1. Choose a database (SQLite, PostgreSQL, MySQL)
2. Install database driver (e.g., `pip install psycopg2-binary` for PostgreSQL)
3. Replace the `responses_db` list in `app.py` with database operations
4. Implement proper session management

## Risk Classification Algorithm

The app uses a binary classification system:

### HIGH RISK Classification

User meets **ANY** of these criteria:

1. **PHQ-2 Score ≥ 3** (Positive depression screen)
2. **Any High-Risk Flag**:
   - Prior mental health treatment
   - Medications for mood/anxiety
   - Fair or Poor general health
3. **PHQ-2 Score = 2 AND Lifestyle Risk ≥ 2** (Borderline symptoms + multiple risk factors)

### LOW RISK Classification

User does not meet any HIGH RISK criteria.

## Clinical Validation

- **PHQ-2**: Validated depression screener (83% sensitivity, 92% specificity)
- **PRAMS Data**: Based on CDC's Pregnancy Risk Assessment Monitoring System (2016-2021, N=178,299)
- **ACOG Guidelines**: Follows American College of Obstetricians and Gynecologists recommendations

## Security & Privacy

### Important Notes

1. **Change Secret Key**: Before deploying to production, change the `secret_key` in `app.py`
2. **HTTPS**: Always use HTTPS in production to encrypt data in transit
3. **Database**: Implement proper database with encryption at rest
4. **HIPAA Compliance**: If handling PHI, ensure full HIPAA compliance
5. **User Consent**: Display clear privacy policy and obtain user consent

### Current Limitations

- Responses stored in memory (lost on server restart)
- No user authentication
- No data encryption
- No audit logging

**For production use, implement proper data storage and security measures.**

## Deployment

### Option 1: Heroku

1. Create `Procfile`:
   ```
   web: gunicorn app:app
   ```

2. Add gunicorn to requirements.txt:
   ```
   pip install gunicorn
   pip freeze > requirements.txt
   ```

3. Deploy:
   ```bash
   heroku create your-app-name
   git push heroku main
   ```

### Option 2: AWS EC2

1. Launch an EC2 instance
2. Install Python and dependencies
3. Use nginx as reverse proxy
4. Run Flask with gunicorn
5. Configure SSL with Let's Encrypt

### Option 3: Docker

1. Create `Dockerfile`:
   ```dockerfile
   FROM python:3.10-slim
   WORKDIR /app
   COPY requirements.txt .
   RUN pip install -r requirements.txt
   COPY . .
   EXPOSE 5000
   CMD ["python", "app.py"]
   ```

2. Build and run:
   ```bash
   docker build -t mental-health-screening .
   docker run -p 5000:5000 mental-health-screening
   ```

## Customization

### Changing Colors

Edit CSS variables in `static/css/style.css`:

```css
:root {
    --primary-color: #4F46E5;  /* Change to your brand color */
    --success-color: #10B981;
    --danger-color: #EF4444;
    /* ... */
}
```

### Adding Logo

1. Add logo image to `static/` folder
2. Update `nav-brand` in `templates/base.html`:
   ```html
   <div class="nav-brand">
       <img src="{{ url_for('static', filename='logo.png') }}" alt="Logo">
       <span>Your Organization Name</span>
   </div>
   ```

### Customizing Output Messages

Edit the results page template in `templates/results.html` or modify the output generation logic in `app.py`.

## Testing

### Manual Testing Checklist

- [ ] All 10 questions display correctly
- [ ] Conditional logic works (Q5b only shows if Q5=Yes)
- [ ] Progress bar updates correctly
- [ ] Previous/Next buttons work
- [ ] PHQ-2 scoring calculates correctly (0-6)
- [ ] High-Risk classification triggers appropriately
- [ ] Low-Risk classification displays correctly
- [ ] Routing matches care setting selection
- [ ] Crisis resources are always visible
- [ ] Dashboard charts display correctly
- [ ] Responsive design works on mobile

### Test Cases

**High Risk Scenarios:**
- PHQ-2 score ≥ 3
- Prior mental health treatment (Yes)
- Fair or Poor health
- Medications for mood/anxiety

**Low Risk Scenarios:**
- PHQ-2 score 0-2
- No high-risk flags
- Fewer than 2 lifestyle risk factors

## Contributing

This application is built for educational and clinical purposes. If you're implementing this for actual clinical use:

1. Consult with mental health professionals
2. Ensure HIPAA compliance
3. Implement proper security measures
4. Consider professional liability insurance
5. Provide clear disclaimers

## Disclaimer

**This screening tool is for informational purposes only and does not constitute a clinical diagnosis.** All users identified as high risk should be referred to qualified mental health professionals for comprehensive evaluation and treatment.

## License

This project is provided as-is for educational purposes. Consult with legal counsel before deploying for clinical use.

## Support & Resources

### Crisis Hotlines (24/7)

- **988 Suicide & Crisis Lifeline**: 988 or 1-800-273-8255
- **Crisis Text Line**: Text HOME to 741741
- **PSI Helpline**: 1-800-944-4773 (perinatal specific)
- **National Maternal MH Hotline**: 1-833-852-6262

### Clinical Resources

- Postpartum Support International: www.postpartum.net
- ACOG Guidelines: www.acog.org
- CDC PRAMS: www.cdc.gov/prams

## Contact

For technical questions or support, please refer to the documentation in the parent directory or consult with your development team.

---

**Built with care for perinatal mental health. 💙**
