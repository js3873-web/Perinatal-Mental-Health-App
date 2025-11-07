# Mental Health Screening App - Implementation Guide

## 📦 What's Included

This folder contains a complete implementation package for a perinatal mental health screening app based on PRAMS Phase 8 data (N=178,299, years 2016-2021) and the PHQ-2 depression screener.

### Core Documentation Files

1. **`variable_categories_analysis.md`** - Detailed analysis of PRAMS variables with frequencies and categories
2. **`variable_categories_summary.md`** - Quick reference guide with risk algorithms
3. **`app_question_flow.md`** - Complete question sequence with UI/UX recommendations
4. **`scoring_algorithm.md`** - Binary risk classification algorithm (Low vs High Risk)
5. **`output_templates.md`** - User-facing output messages for both risk tiers

### Implementation Files

6. **`questions_config.json`** - Machine-readable configuration for developers
7. **`questions_simple.csv`** - Spreadsheet view of all questions
8. **`variable_categories.csv`** - Lookup table for PRAMS category labels

### Supporting Files

9. **`PRAMS_Phase_8_Standard_Section_L_Codebook.docx`** - Official codebook (reference)
10. **`phase8_2016_2021_std_l.sas7bdat`** - Source data (146MB)

---

## 🚀 Quick Start Guide

### For Product Managers / Designers

**Start Here:**
1. Read `app_question_flow.md` - Understand the full user journey
2. Review `output_templates.md` - See what users will receive at the end
3. Check `variable_categories_summary.md` - Understand the risk model

**Key Decisions to Make:**
- App platform (mobile web vs native app)
- Data storage approach (local vs server-side)
- HIPAA compliance requirements
- Integration with existing EHR/referral systems

---

### For Developers

**Start Here:**
1. Import `questions_config.json` into your codebase
2. Implement the question flow logic (see JSON structure)
3. Build the scoring algorithm using pseudocode in `scoring_algorithm.md`
4. Create output templates based on `output_templates.md`

**JSON Structure Overview:**
```javascript
{
  "screening_metadata": { ... },        // Version, timing, risk levels
  "sections": [ ... ],                   // 5 sections with 11 questions total
  "scoring_components": { ... },         // PHQ2_Total, High_Risk_Flags, Lifestyle_Risk
  "classification_rules": { ... },       // Binary: LOW_RISK vs HIGH_RISK
  "routing_logic": { ... },              // Personalized referrals
  "crisis_resources": { ... }            // 24/7 hotlines
}
```

**Sample Implementation (Pseudocode):**
```javascript
// 1. Load questions from JSON
const config = require('./questions_config.json');

// 2. Present questions to user
function displayQuestion(questionId) {
  const question = findQuestionById(questionId);
  // Check display_condition for conditional questions
  if (question.conditional && !meetsDisplayCondition(question)) {
    return skipToNext(question);
  }
  // Render question with response_options
  render(question);
}

// 3. Calculate scores
function calculateRisk(responses) {
  // PHQ-2 Total
  const phq2_total = responses.PHQ2_Q1.score + responses.PHQ2_Q2.score;

  // High-Risk Flags
  const flags = {
    prior_mh: responses.BPG_MH.value === 2,
    mh_meds: responses.PRE_RX.value === 2 &&
             ['Yes', 'Not sure'].includes(responses.PRE_RX_MH.value),
    poor_health: responses.HTH_GEN.value >= 4
  };
  const high_risk_flags = Object.values(flags).filter(Boolean).length;

  // Lifestyle Risk
  let lifestyle_risk = 0;
  if (responses.PRE_EXER.value === 1) lifestyle_risk++;
  if (responses.PRE_DIET.value === 2) lifestyle_risk++;
  if (responses.OWGT_OBS.value === 2) lifestyle_risk++;

  // Apply Classification Rules
  if (phq2_total >= 3) return 'HIGH_RISK';
  if (high_risk_flags >= 1) return 'HIGH_RISK';
  if (phq2_total === 2 && lifestyle_risk >= 2) return 'HIGH_RISK';
  return 'LOW_RISK';
}

// 4. Generate output
function generateOutput(riskLevel, responses) {
  const routing = determineRouting(responses.BPG_TALK, responses.FLU_SRC);
  const template = loadTemplate(riskLevel, routing);
  return renderOutput(template, responses);
}
```

---

### For Data Scientists / Researchers

**Start Here:**
1. Review `variable_categories_analysis.md` for data distribution
2. Check `scoring_algorithm.md` for algorithm validation
3. Source data available in `phase8_2016_2021_std_l.sas7bdat`

**Validation Metrics:**
- PHQ-2 ≥3: 83% sensitivity, 92% specificity (literature)
- Our algorithm: ~95% sensitivity, ~75% specificity (estimated)
- Trade-off: Prioritize sensitivity for perinatal population

**Expected Classification:**
- High Risk: 15-20% of users
- Low Risk: 80-85% of users

---

## 📋 Question Flow Summary

### Total Questions: 10 (9-10 depending on skip logic)

**Section 1: PHQ-2 Screening (2 questions)**
- Q1: Depressed mood (0-3 points)
- Q2: Loss of interest (0-3 points)

**Section 2: Mental Health History (1 question)**
- Q3: Prior MH treatment (HIGH RISK if Yes)

**Section 3: Health Status (2-3 questions)**
- Q4: General health (RISK if Fair/Poor)
- Q5: Prescription medications
- Q5b: For mood/anxiety? (CONDITIONAL - only if Q5=Yes)

**Section 4: Lifestyle Factors (3 questions)**
- Q6: Exercise habits (modest risk if No)
- Q7: Dieting behavior (modest risk if Yes)
- Q8: Overweight/obesity (modest risk if Yes)

**Section 5: Healthcare Access (2 questions)**
- Q9: Existing provider relationship (for routing)
- Q10: Typical care setting (for routing)

**Estimated Time:** 10-15 minutes

---

## 🎯 Risk Classification Algorithm

### Binary System: LOW RISK vs HIGH RISK

**HIGH RISK Classification:**
User meets **ANY** of these criteria:
1. **PHQ-2 ≥ 3** (Positive depression screen)
2. **Any High-Risk Flag:**
   - Prior mental health treatment (BPG_MH = Yes)
   - Medications for mood/anxiety (PRE_RX_MH = Yes/Not sure)
   - Fair or Poor general health (HTH_GEN = 4 or 5)
3. **Borderline symptoms + Multiple lifestyle risks:**
   - PHQ-2 = 2 AND Lifestyle Risk ≥ 2

**LOW RISK Classification:**
- Does not meet any HIGH RISK criteria

### Scoring Components

| Component | Range | Source |
|-----------|-------|--------|
| PHQ-2 Total | 0-6 | Q1 + Q2 scores |
| High-Risk Flags | 0-3 | BPG_MH, PRE_RX_MH, HTH_GEN |
| Lifestyle Risk | 0-3 | PRE_EXER, PRE_DIET, OWGT_OBS |

---

## 📤 Output Structure

### For LOW RISK Users:
1. **Risk Score/Category** - "You're doing well" message
2. **Provider Referrals** - Preventive care recommendations
3. **Self-Help Resources** - Education, apps, support groups
4. **Crisis Resources** - 24/7 hotlines (always included)

### For HIGH RISK Users:
1. **Risk Score/Category** - "Action recommended" urgent message
2. **Provider Referrals** - Personalized by care setting, 24-48hr urgency
3. **Self-Help Resources** - Symptom management while waiting for care
4. **Crisis Resources** - Emphasized, with safety planning

### Personalized Routing (Based on FLU_SRC)

| User's Care Setting | Referral Type |
|---------------------|---------------|
| OB/Gyn office | OB/Gyn with integrated behavioral health |
| Family doctor | Primary care with MH services |
| Community clinic | FQHC / Public clinics + hotlines |
| Hospital | Hospital-based behavioral health |
| Pharmacy | Telehealth + pharmacy walk-in services |
| Work/school | EAP / Occupational health resources |
| Other/None | Telehealth + community resources |

---

## 🔐 Privacy & Compliance

### Data Sensitivity
All collected data is **Protected Health Information (PHI)** under HIPAA:
- Depression screening results
- Mental health treatment history
- Medication information
- Health status

### Compliance Requirements
1. **HIPAA Compliance** - Required for healthcare data
2. **Consent & Authorization** - Clear opt-in before data collection
3. **Encryption** - At rest and in transit
4. **Access Controls** - Audit logging for all data access
5. **Data Retention** - Define retention and deletion policies
6. **User Rights** - Allow data download and deletion

### Recommended Approach
- **Option A:** Anonymous screening (no user identification)
  - Pros: No HIPAA compliance needed
  - Cons: Can't save progress, no follow-up

- **Option B:** User accounts with PHI
  - Pros: Save progress, longitudinal tracking
  - Cons: Full HIPAA compliance required

---

## 🧪 Testing Checklist

### Functional Testing
- [ ] All 10 questions display correctly
- [ ] Skip logic works (Q5b conditional on Q5)
- [ ] PHQ-2 scoring calculates correctly (0-6)
- [ ] High-Risk Flags trigger appropriately
- [ ] Lifestyle Risk sums correctly (0-3)
- [ ] Classification algorithm works for all edge cases
- [ ] Routing logic matches FLU_SRC to correct referral type
- [ ] Crisis resources always display

### Edge Cases
- [ ] User answers "Prefer not to answer" to all questions
- [ ] User skips Q5b (PRE_RX = No)
- [ ] PHQ-2 = 0 but all high-risk flags present
- [ ] PHQ-2 = 6 (maximum score)
- [ ] Exactly at thresholds (PHQ-2 = 2, 3; Lifestyle = 1, 2)

### UI/UX Testing
- [ ] Questions readable on mobile devices
- [ ] Progress indicator updates correctly
- [ ] Back button allows changing previous answers
- [ ] Output displays correctly for both risk levels
- [ ] Crisis hotline buttons work (click-to-call on mobile)
- [ ] Print/PDF/Email functionality works

### Accessibility Testing
- [ ] Screen reader compatible
- [ ] Keyboard navigation works
- [ ] Color contrast meets WCAG AA standards
- [ ] Text resizable without breaking layout
- [ ] Alternative text for all images/icons

---

## 📊 Expected Results Distribution

Based on PRAMS data (N=178,299):

### Risk Factor Prevalence
| Factor | Prevalence | Count |
|--------|------------|-------|
| PHQ-2 ≥3 (estimated) | 10-12% | ~17,830 - 21,396 |
| Prior MH treatment | 2.17% | 3,873 |
| Fair/Poor health | 1.05% | 1,872 |
| Meds for mood/anxiety | 1-2% | ~1,780 - 3,566 |
| No regular exercise | 17.76% | 31,671 |
| Dieting | 8.31% | 14,817 |
| Overweight/obese | 1.56% | 2,786 |

### Projected Classification
- **HIGH RISK**: 15-20% of users (~26,745 - 35,660)
- **LOW RISK**: 80-85% of users (~142,639 - 151,554)

### Missing Data
All PRAMS variables have 70-97% missing data. This is **normal** due to:
- Survey skip patterns
- State-specific questions
- Respondent non-response

**App Design Implication:** Make all questions optional with "Prefer not to answer"

---

## 🔄 Version History

| Version | Date | Changes |
|---------|------|---------|
| 1.0 | 2025-10-31 | Initial implementation package |

---

## 📚 References

### Clinical Validation
1. Kroenke K, Spitzer RL, Williams JB. The Patient Health Questionnaire-2: validity of a two-item depression screener. *Med Care*. 2003;41(11):1284-92.

2. ACOG Committee Opinion No. 757: Screening for perinatal depression. *Obstet Gynecol*. 2018;132(5):e208-e212.

3. Cox JL, Holden JM, Sagovsky R. Detection of postnatal depression. Development of the 10-item Edinburgh Postnatal Depression Scale. *Br J Psychiatry*. 1987;150:782-6.

### Data Source
4. Pregnancy Risk Assessment Monitoring System (PRAMS), Phase 8 Automated Research File, Centers for Disease Control and Prevention, 2016-2021. N=178,299.

### Perinatal Mental Health Resources
5. Postpartum Support International: www.postpartum.net
6. National Maternal Mental Health Hotline: 1-833-TLC-MAMA
7. ACOG Perinatal Mental Health Toolkit: www.acog.org

---

## 🤝 Support & Contact

### For Technical Questions
- Review the detailed documentation in each markdown file
- Check `questions_config.json` for implementation details

### For Clinical Questions
- Consult with a perinatal mental health specialist
- Review ACOG guidelines on perinatal depression screening

### For Data Questions
- Refer to official PRAMS documentation: www.cdc.gov/prams
- Contact CDC PRAMS team for additional codebook questions

---

## ⚠️ Important Disclaimers

1. **Not a Diagnostic Tool**: This screening tool is for **informational purposes only** and does not constitute a clinical diagnosis. All users identified as high risk should be referred to qualified mental health professionals.

2. **Clinical Oversight Required**: Implementation of this screening tool should be overseen by licensed healthcare professionals familiar with perinatal mental health.

3. **Local Adaptation Needed**: Provider referral lists and resources should be customized to your local area and healthcare system.

4. **Regular Updates Required**: Crisis hotlines, resource links, and clinical guidelines should be reviewed and updated regularly (recommend quarterly).

5. **Risk Management**: Ensure clear protocols for handling high-risk users, including same-day follow-up and crisis intervention procedures.

---

## 🎯 Implementation Roadmap

### Phase 1: MVP (Minimum Viable Product)
- [ ] Implement 10-question flow
- [ ] Build binary risk classifier
- [ ] Create basic output templates
- [ ] Include crisis resources
- [ ] Basic analytics (risk classification distribution)

**Timeline:** 4-6 weeks

### Phase 2: Enhanced Features
- [ ] User accounts (save/resume screening)
- [ ] Automated referrals (integrate with EHR)
- [ ] Provider dashboard
- [ ] Longitudinal tracking (re-screening at intervals)
- [ ] Push notifications for follow-ups

**Timeline:** 8-12 weeks

### Phase 3: Advanced Analytics
- [ ] Predictive modeling
- [ ] Personalized interventions
- [ ] Integration with wearables (sleep, activity tracking)
- [ ] Outcome tracking (did user access care?)
- [ ] Population health reporting

**Timeline:** 12-16 weeks

---

## 📞 Crisis Resources (Always Include)

Every implementation **MUST** prominently display these 24/7 resources:

### Immediate Help
- **988 Suicide & Crisis Lifeline**: 988 or 1-800-273-8255
- **Crisis Text Line**: Text HOME to 741741
- **PSI Helpline**: 1-800-944-4773 (perinatal specific)
- **National Maternal MH Hotline**: 1-833-TLC-MAMA (1-833-852-6262)

### Emergency
- **911** for life-threatening emergencies
- **Nearest Hospital Emergency Department**

---

**Good luck with your implementation! This screening tool has the potential to identify and help thousands of individuals experiencing perinatal mood disorders. 🌟**
