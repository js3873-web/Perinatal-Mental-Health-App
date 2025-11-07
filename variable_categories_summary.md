# PRAMS Phase 8 Section L - Variable Categories Summary
## Verified from Official Codebook

---

## 📊 Quick Reference Table

| Variable | Question Topic | Format | Key Categories | High-Risk Values |
|----------|---------------|--------|----------------|------------------|
| **BPG_MH** | Prior MH treatment | NYS1F | 1=NO, 2=YES | **2 (YES)** = 3,873 (2.17%) |
| **HTH_GEN** | General health | HTH_GEN | 1-5 scale | **4,5 (Fair/Poor)** = 1,872 (1.05%) |
| **PRE_RX** | Pre-pregnancy meds | NY1F | 1=NO, 2=YES | **2 (YES)** = 12,556 (7.04%) |
| **OWGT_OBS** | Overweight/obese | NY1F | 1=NO, 2=YES | **2 (YES)** = 2,786 (1.56%) |
| **PRE_EXER** | Exercise 3+ days/wk | NY1F | 1=NO, 2=YES | **1 (NO)** = 31,671 (17.76%) |
| **PRE_DIET** | Dieting | NY1F | 1=NO, 2=YES | **2 (YES)** = 14,817 (8.31%) |
| **BPG_TALK** | HCW discussed pregnancy | NY1F | 1=NO, 2=YES | **2 (YES)** = 14,952 (8.39%) |
| **FLU_SRC** | Flu shot location | FLU_SRC | 1-7 categories | All valid responses |

---

## 📋 Detailed Category Mappings

### 1. BPG_MH - Mental Health Treatment Before Pregnancy
**Codebook Definition**: "Pre-preg -- counseling or tx for MH"

```
Value 1 = NO     →  9,901 respondents (5.55%)
Value 2 = YES    →  3,873 respondents (2.17%) ⚠️ HIGH RISK
Missing         → 164,525 (92.27%)
```

**App Implementation**:
```
Question: "Before you got pregnant, did you receive counseling or treatment
from a health care worker for depression, anxiety, or other mental health
conditions?"

Options:
○ Yes  [IF SELECTED → HIGH RISK FLAG + Immediate screening]
○ No
○ Prefer not to answer
```

---

### 2. HTH_GEN - General Health Status
**Codebook Definition**: "General Health"

```
Value 1 = EXCELLENT   →  6,387 respondents (3.58%)
Value 2 = VERY GOOD   →  8,620 respondents (4.83%)
Value 3 = GOOD        →  6,585 respondents (3.69%)
Value 4 = FAIR        →  1,705 respondents (0.96%) ⚠️ RISK AMPLIFIER
Value 5 = POOR        →    167 respondents (0.09%) ⚠️ RISK AMPLIFIER
Missing               → 154,835 (86.84%)
```

**App Implementation**:
```
Question: "In general, how would you describe your health before you got pregnant?"

Options:
○ Excellent
○ Very Good
○ Good
○ Fair      [IF SELECTED → Elevate to Moderate/High Risk]
○ Poor      [IF SELECTED → Elevate to High Risk]
```

---

### 3. PRE_RX - Pre-pregnancy Prescription Medications
**Codebook Definition**: "Pre-pregnancy prescrip meds"

```
Value 1 = NO     → 40,497 respondents (22.71%)
Value 2 = YES    → 12,556 respondents (7.04%) ⚠️ NEEDS FOLLOW-UP
Missing          → 125,246 (70.24%)
```

**App Implementation** (Two-step):
```
Question 1: "In the month before you got pregnant, were you taking any
prescription medications?"

Options:
○ Yes  [IF SELECTED → Show Question 2]
○ No
○ Prefer not to answer

---

Question 2 (CONDITIONAL): "Were any of these medications for depression,
anxiety, or other mental health conditions?"

Options:
○ Yes          [IF SELECTED → HIGH RISK FLAG]
○ No
○ Not sure     [IF SELECTED → HIGH RISK FLAG (conservative approach)]
```

---

### 4. OWGT_OBS - Overweight/Obesity
**Codebook Definition**: "Health problem - overweight/obese"

```
Value 1 = NO     →  5,539 respondents (3.11%)
Value 2 = YES    →  2,786 respondents (1.56%) ⚠️ MODEST AMPLIFIER
Missing          → 169,974 (95.33%)
```

**App Implementation**:
```
Question: "Before you got pregnant, did you have any of the following
health problems: overweight or obesity?"

Options:
○ Yes  [IF SELECTED → Add modest risk points]
○ No
○ Prefer not to answer
```

---

### 5. PRE_EXER - Pre-pregnancy Exercise
**Codebook Definition**: "Pre-pregnancy exercise 3+ days/wk"

```
Value 1 = NO     → 31,671 respondents (17.76%) ⚠️ MODEST AMPLIFIER
Value 2 = YES    → 21,407 respondents (12.01%) [PROTECTIVE]
Missing          → 125,221 (70.23%)
```

**App Implementation**:
```
Question: "During the month before you got pregnant, did you exercise for
at least 30 minutes on 3 or more days per week?"

Options:
○ Yes  [IF SELECTED → Protective factor]
○ No   [IF SELECTED → Add modest risk points]
○ Prefer not to answer
```

---

### 6. PRE_DIET - Pre-pregnancy Dieting
**Codebook Definition**: "Pre-pregnancy dieting"

```
Value 1 = NO     → 38,303 respondents (21.48%)
Value 2 = YES    → 14,817 respondents (8.31%) ⚠️ MODEST AMPLIFIER
Missing          → 125,179 (70.21%)
```

**App Implementation**:
```
Question: "In the month before you got pregnant, were you trying to lose
weight or control your weight by dieting?"

Options:
○ Yes  [IF SELECTED → Add modest risk points (body image concerns)]
○ No
○ Prefer not to answer
```

---

### 7. BPG_TALK - Healthcare Worker Discussion
**Codebook Definition**: "HCW discussed preparing for pregnancy"

```
Value 1 = NO     → 38,516 respondents (21.60%)
Value 2 = YES    → 14,952 respondents (8.39%) ✓ EXISTING CONNECTION
Missing          → 124,831 (70.01%)
```

**App Implementation**:
```
Question: "Before you got pregnant, did a health care worker talk with
you about preparing for pregnancy?"

Options:
○ Yes  [IF SELECTED → User has existing provider relationship;
                     prioritize referral to this provider]
○ No
○ Prefer not to answer
```

---

### 8. FLU_SRC - Healthcare Access Location
**Codebook Definition**: "Where flu shot was given"

```
Value 1 = OBGYN OFFICE          →  1,899 respondents (1.07%)
Value 2 = FAMILY DR. OFFICE     →    756 respondents (0.42%)
Value 3 = HEALTH DEPT./CLINIC   →    241 respondents (0.14%)
Value 4 = HOSPITAL              →    745 respondents (0.42%)
Value 5 = PHARMACY/STORE        →    536 respondents (0.30%)
Value 6 = WORK/SCHOOL           →    379 respondents (0.21%)
Value 7 = OTHER                 →     82 respondents (0.05%)
Missing                         → 173,661 (97.40%)
```

**App Implementation** (Routing proxy):
```
Question: "Where do you typically receive healthcare services?
(Select the place you visit most often)"

Options:
○ OB/Gyn office              [Route to → Local OB/Gyn with behavioral health]
○ Family doctor/PCP          [Route to → PCP with behavioral health]
○ Community health clinic    [Route to → Public clinics + hotlines]
○ Hospital                   [Route to → Hospital behavioral health services]
○ Pharmacy                   [Route to → Pharmacy walk-in + telehealth]
○ Work/school clinic         [Route to → Occupational health resources]
○ Other
○ I don't regularly visit    [Route to → Telehealth + crisis lines]
   any healthcare provider
```

---

## 🎯 Risk Scoring Algorithm

### HIGH RISK (Immediate screening + same-day care options)
Any of the following:
- **BPG_MH = 2 (YES)** - Prior mental health treatment
- **PRE_RX = 2 (YES)** + medication was for mood/anxiety
- **HTH_GEN = 4 or 5** - Fair or Poor general health
- **Positive PHQ-2** - ≥2 on depression screener

### MODERATE RISK (Full screening + appointment within 1-3 days)
- **Positive PHQ-2** alone (without other high-risk factors)
- Multiple lifestyle modifiers:
  - PRE_EXER = 1 (No exercise)
  - PRE_DIET = 2 (Dieting)
  - OWGT_OBS = 2 (Overweight/obese)

### LOW RISK (Education + self-monitoring + re-screen in 2 weeks)
- Negative PHQ-2
- Few or no risk modifiers

---

## 🗺️ Routing Logic

### Priority 1: Existing Provider Connection
If **BPG_TALK = 2 (YES)**:
- User already has a healthcare relationship
- Route to existing provider first
- Use FLU_SRC as secondary confirmation

### Priority 2: Match Familiar Care Setting
Use **FLU_SRC** to determine care preference:

| FLU_SRC Value | Care Setting | Referral Type |
|---------------|--------------|---------------|
| 1 | OB/Gyn office | OB/Gyn with integrated behavioral health |
| 2 | Family doctor | Primary care with MH services |
| 3 | Health dept/clinic | Public clinics + crisis hotlines |
| 4 | Hospital | Hospital-based behavioral health |
| 5 | Pharmacy | Pharmacy walk-in + teletherapy |
| 6 | Work/school | Occupational/student health resources |
| 7 | Other | General telehealth + hotlines |

---

## 📉 Data Quality Notes

### Missing Data Rates
All variables have **70-97% missing data**. This is normal for PRAMS data because:
1. Skip patterns in questionnaires
2. State-specific questions (e.g., PRE_DEPR is CT only)
3. Respondent non-response

### App Design Implications
1. **Make all questions optional** with "Prefer not to answer"
2. **Use progressive disclosure** - only ask follow-ups when relevant
3. **Never require all questions** - work with partial data
4. **Provide value even with minimal responses**

---

## 🚦 Implementation Checklist

### Phase 1: Symptom Gate (2 questions)
- [ ] PHQ-2 Question 1: Down/depressed/hopeless
- [ ] PHQ-2 Question 2: Little interest/pleasure

### Phase 2: High-Risk Screening (3 questions)
- [ ] BPG_MH - Prior mental health treatment
- [ ] HTH_GEN - General health status
- [ ] PRE_RX + follow-up - Medications

### Phase 3: Risk Amplifiers (Optional, 3 questions)
- [ ] OWGT_OBS - Overweight/obesity
- [ ] PRE_EXER - Exercise habits
- [ ] PRE_DIET - Dieting behavior

### Phase 4: Routing Information (2 questions)
- [ ] BPG_TALK - Existing provider relationship
- [ ] FLU_SRC - Typical care setting

---

## 📱 Sample App Flow

```
START
  ↓
[PHQ-2 Screener] (2 questions)
  ↓
  ├─→ NEGATIVE → Continue to risk assessment
  └─→ POSITIVE → FLAG as High Risk, continue assessment
       ↓
[Prior MH Treatment?] (BPG_MH)
  ↓
  └─→ YES → FLAG as High Risk
       ↓
[General Health?] (HTH_GEN)
  ↓
  └─→ Fair/Poor → ELEVATE risk
       ↓
[Prescription Meds?] (PRE_RX)
  ↓
  └─→ YES → [For mood/anxiety?]
              └─→ YES/Unsure → FLAG as High Risk
       ↓
[Optional: Lifestyle factors] (OWGT_OBS, PRE_EXER, PRE_DIET)
  ↓
[Existing provider?] (BPG_TALK)
[Typical care setting?] (FLU_SRC)
  ↓
TRIAGE:
  ├─→ HIGH RISK → In-app EPDS/PHQ-9 + Same-day care + Crisis resources
  ├─→ MODERATE → Full screening + 1-3 day appointment + Education
  └─→ LOW RISK → Education + Self-monitoring + Re-screen in 2 weeks
```

---

## ✅ Validation Status

- ✅ Variable names confirmed from dataset
- ✅ Category codes verified from PRAMS Phase 8 Codebook
- ✅ Frequency distributions calculated from actual data
- ✅ All 9 variables mapped and documented
- ⚠️ PRE_DEPR unavailable (CT-only variable, 100% missing)

**Dataset**: `phase8_2016_2021_std_l.sas7bdat` (N=178,299)
**Codebook**: `PRAMS_Phase_8_Standard_Section_L_Codebook.docx`

---

*Last Updated: October 31, 2025*
