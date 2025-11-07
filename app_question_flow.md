# Mental Health Screening App - Question Flow

## Overview
- **Total Questions**: 10 (2 PHQ-2 + 8 PRAMS variables)
- **Estimated Time**: 10-15 minutes
- **Risk Classification**: Binary (Low Risk vs High Risk)
- **Output**: Risk category + Provider referrals + Self-help resources + Crisis resources

---

## Question Sequence

### 📋 SECTION 1: Depression Screening (PHQ-2)
*Start with validated clinical screener*

---

#### **Q1: Depressed Mood**
**Question ID**: `PHQ2_Q1`

> "Over the past 2 weeks, how often have you felt **down, depressed, or hopeless**?"

**Response Options**:
- ○ Not at all *(Score: 0)*
- ○ Several days *(Score: 1)*
- ○ More than half the days *(Score: 2)*
- ○ Nearly every day *(Score: 3)*
- ○ Prefer not to answer *(Score: null)*

**Scoring**: 0-3 points

---

#### **Q2: Loss of Interest/Pleasure**
**Question ID**: `PHQ2_Q2`

> "Over the past 2 weeks, how often have you had **little interest or pleasure in doing things**?"

**Response Options**:
- ○ Not at all *(Score: 0)*
- ○ Several days *(Score: 1)*
- ○ More than half the days *(Score: 2)*
- ○ Nearly every day *(Score: 3)*
- ○ Prefer not to answer *(Score: null)*

**Scoring**: 0-3 points

**PHQ-2 Total Score**: Sum of Q1 + Q2 (Range: 0-6)
- **0-2**: Negative screen (Low risk for depression)
- **3+**: Positive screen (**HIGH RISK FLAG** - requires follow-up)

---

### 🏥 SECTION 2: Mental Health History

---

#### **Q3: Prior Mental Health Treatment**
**Question ID**: `BPG_MH`
**Variable**: BPG_MH (Value 2=YES is high risk)

> "Before you got pregnant, did you receive **counseling or treatment from a health care worker** for depression, anxiety, or other mental health conditions?"

**Response Options**:
- ○ Yes *(HIGH RISK FLAG)*
- ○ No
- ○ Prefer not to answer

**Risk Impact**: If YES → **Automatic High Risk classification**

---

### 💊 SECTION 3: Health Status

---

#### **Q4: General Health**
**Question ID**: `HTH_GEN`
**Variable**: HTH_GEN (Values 4-5 are risk amplifiers)

> "In general, how would you describe your **health before you got pregnant**?"

**Response Options**:
- ○ Excellent
- ○ Very Good
- ○ Good
- ○ Fair *(RISK AMPLIFIER)*
- ○ Poor *(RISK AMPLIFIER)*
- ○ Prefer not to answer

**Risk Impact**: Fair/Poor → **Elevate to High Risk** (especially if combined with positive PHQ-2)

---

#### **Q5: Prescription Medications (Part 1)**
**Question ID**: `PRE_RX`
**Variable**: PRE_RX (Value 2=YES triggers follow-up)

> "In the month before you got pregnant, were you taking any **prescription medications**?"

**Response Options**:
- ○ Yes *(Shows Q5b)*
- ○ No *(Skip to Q6)*
- ○ Prefer not to answer *(Skip to Q6)*

**Skip Logic**: If NO or Prefer not to answer → Skip Q5b, go to Q6

---

#### **Q5b: Medication Type (CONDITIONAL)**
**Question ID**: `PRE_RX_MH`
**Variable**: Derived from PRE_RX

> "Were any of these medications for **depression, anxiety, or other mental health conditions**?"

**Response Options**:
- ○ Yes *(HIGH RISK FLAG)*
- ○ No
- ○ Not sure *(HIGH RISK FLAG - conservative approach)*

**Risk Impact**: If YES or Not sure → **Automatic High Risk classification**

**Display Condition**: Only shown if Q5 = "Yes"

---

### 🏃 SECTION 4: Lifestyle Factors

---

#### **Q6: Exercise Habits**
**Question ID**: `PRE_EXER`
**Variable**: PRE_EXER (Value 1=NO is modest risk)

> "During the month before you got pregnant, did you **exercise for at least 30 minutes on 3 or more days per week**?"

**Response Options**:
- ○ Yes *(Protective factor)*
- ○ No *(Modest risk amplifier)*
- ○ Prefer not to answer

**Risk Impact**: No → Add +1 to lifestyle risk score

---

#### **Q7: Dieting Behavior**
**Question ID**: `PRE_DIET`
**Variable**: PRE_DIET (Value 2=YES is modest risk)

> "In the month before you got pregnant, were you trying to **lose weight or control your weight by dieting**?"

**Response Options**:
- ○ Yes *(Modest risk amplifier - body image concerns)*
- ○ No
- ○ Prefer not to answer

**Risk Impact**: Yes → Add +1 to lifestyle risk score

---

#### **Q8: Weight Status**
**Question ID**: `OWGT_OBS`
**Variable**: OWGT_OBS (Value 2=YES is modest risk)

> "Before you got pregnant, did you have any of the following health problems: **overweight or obesity**?"

**Response Options**:
- ○ Yes *(Modest risk amplifier)*
- ○ No
- ○ Prefer not to answer

**Risk Impact**: Yes → Add +1 to lifestyle risk score

**Lifestyle Risk Score**: Sum of Q6-Q8 risk factors (Range: 0-3)

---

### 🩺 SECTION 5: Healthcare Access (For Routing)

---

#### **Q9: Existing Healthcare Relationship**
**Question ID**: `BPG_TALK`
**Variable**: BPG_TALK (Value 2=YES indicates existing connection)

> "Before you got pregnant, did a **health care worker talk with you about preparing for pregnancy**?"

**Response Options**:
- ○ Yes *(Indicates existing provider relationship)*
- ○ No
- ○ Prefer not to answer

**Routing Impact**: If YES → Prioritize referral to existing provider

---

#### **Q10: Typical Healthcare Setting**
**Question ID**: `FLU_SRC`
**Variable**: FLU_SRC (Used as proxy for care preference)

> "Where do you **typically receive healthcare services**? (Select the place you visit most often)"

**Response Options**:
- ○ OB/Gyn office
- ○ Family doctor / Primary care physician
- ○ Community health clinic
- ○ Hospital
- ○ Pharmacy
- ○ Work or school clinic
- ○ Other
- ○ I don't regularly visit any healthcare provider

**Routing Impact**: Match referral destination to user's familiar care setting

---

## 🎯 Risk Scoring Algorithm

### Step 1: Calculate Component Scores

#### A. PHQ-2 Score
```
PHQ2_Total = Q1_Score + Q2_Score
Range: 0-6
Positive Screen: ≥3
```

#### B. High-Risk Flags (Boolean)
```
Flag 1: BPG_MH = "Yes" (Prior MH treatment)
Flag 2: PRE_RX_MH = "Yes" OR "Not sure" (Meds for mood/anxiety)
Flag 3: HTH_GEN = "Fair" OR "Poor" (Poor general health)

High_Risk_Flags = Count of true flags (Range: 0-3)
```

#### C. Lifestyle Risk Score
```
Lifestyle_Risk = 0
If PRE_EXER = "No": +1
If PRE_DIET = "Yes": +1
If OWGT_OBS = "Yes": +1

Range: 0-3
```

---

### Step 2: Binary Classification Rules

#### **HIGH RISK** (Requires immediate attention)
User is classified as **High Risk** if **ANY** of the following:

1. **PHQ-2 Score ≥ 3** (Positive depression screen)

2. **Any High-Risk Flag = True**:
   - Prior mental health treatment (BPG_MH = Yes)
   - Taking/took meds for mood/anxiety (PRE_RX_MH = Yes/Not sure)
   - Fair or Poor general health (HTH_GEN = Fair/Poor)

3. **PHQ-2 Score = 2 AND Lifestyle_Risk ≥ 2**
   (Borderline symptoms with multiple risk factors)

#### **LOW RISK** (No immediate concern)
User is classified as **Low Risk** if **ALL** of the following:

1. PHQ-2 Score ≤ 2 (Negative or borderline screen)
2. No High-Risk Flags
3. Lifestyle_Risk < 2 (Fewer than 2 lifestyle risk factors)

---

### Step 3: Routing Information

#### Existing Provider Connection
```
If BPG_TALK = "Yes":
  Priority = "Existing Provider"
Else:
  Priority = "New Referral"
```

#### Care Setting Preference
```
Match FLU_SRC response to referral type:
  - OB/Gyn office → OB/Gyn with behavioral health
  - Family doctor → Primary care with MH services
  - Community clinic → Public clinics + hotlines
  - Hospital → Hospital behavioral health
  - Pharmacy → Pharmacy walk-in + telehealth
  - Work/school → Occupational health resources
  - Other/None → Telehealth + crisis lines
```

---

## 📊 Question Flow Diagram

```
START
  ↓
┌─────────────────────────────────────┐
│ SECTION 1: PHQ-2 Screening          │
│ Q1: Depressed mood (0-3 pts)        │
│ Q2: Loss of interest (0-3 pts)      │
│                                     │
│ Total: 0-6 pts                      │
└─────────────────────────────────────┘
  ↓
  ├─→ Score ≥3? → FLAG: High Risk
  └─→ Score <3? → Continue assessment
  ↓
┌─────────────────────────────────────┐
│ SECTION 2: Mental Health History    │
│ Q3: Prior MH treatment (BPG_MH)     │
└─────────────────────────────────────┘
  ↓
  └─→ YES? → FLAG: High Risk
  ↓
┌─────────────────────────────────────┐
│ SECTION 3: Health Status             │
│ Q4: General health (HTH_GEN)        │
│ Q5: Prescription meds (PRE_RX)      │
│   └→ Q5b: For mood/anxiety?         │
│         (if Q5=Yes)                 │
└─────────────────────────────────────┘
  ↓
  ├─→ Q4=Fair/Poor? → FLAG: High Risk
  └─→ Q5b=Yes/Unsure? → FLAG: High Risk
  ↓
┌─────────────────────────────────────┐
│ SECTION 4: Lifestyle Factors         │
│ Q6: Exercise (PRE_EXER)             │
│ Q7: Dieting (PRE_DIET)              │
│ Q8: Overweight/obese (OWGT_OBS)     │
│                                     │
│ Lifestyle Risk Score: 0-3           │
└─────────────────────────────────────┘
  ↓
┌─────────────────────────────────────┐
│ SECTION 5: Healthcare Access         │
│ Q9: Existing provider (BPG_TALK)    │
│ Q10: Typical care setting (FLU_SRC) │
└─────────────────────────────────────┘
  ↓
┌─────────────────────────────────────┐
│ CALCULATE RISK CLASSIFICATION        │
│                                     │
│ Apply Binary Algorithm:             │
│ - Check PHQ-2 score                 │
│ - Check High-Risk Flags             │
│ - Check Lifestyle Risk Score        │
└─────────────────────────────────────┘
  ↓
  ├───────────────────┬───────────────────┐
  ↓                   ↓                   ↓
LOW RISK          HIGH RISK
  ↓                   ↓
Display:          Display:
• Risk category   • Risk category
• Education       • Urgent message
• Prevention      • Provider referrals
• Resources       • Crisis hotlines
                  • Self-help resources
```

---

## 🔄 Skip Logic Summary

| Question | Display Condition | Skip To |
|----------|------------------|---------|
| Q1 | Always shown | Q2 |
| Q2 | Always shown | Q3 |
| Q3 | Always shown | Q4 |
| Q4 | Always shown | Q5 |
| Q5 | Always shown | Q5b or Q6 |
| **Q5b** | **Only if Q5 = "Yes"** | **Q6** |
| Q6 | Always shown | Q7 |
| Q7 | Always shown | Q8 |
| Q8 | Always shown | Q9 |
| Q9 | Always shown | Q10 |
| Q10 | Always shown | Results |

**Total Conditional Questions**: 1 (Q5b)
**Minimum Questions**: 9 (if Q5 ≠ Yes)
**Maximum Questions**: 10 (if Q5 = Yes)

---

## ⏱️ Estimated Completion Time

| Section | Questions | Est. Time |
|---------|-----------|-----------|
| PHQ-2 Screening | 2 | 1-2 min |
| Mental Health History | 1 | 30 sec |
| Health Status | 2-3 | 2-3 min |
| Lifestyle Factors | 3 | 2-3 min |
| Healthcare Access | 2 | 1-2 min |
| **Total** | **9-10** | **10-15 min** |

---

## 📝 Data Collection Format

### Response Data Structure
```json
{
  "user_id": "string",
  "timestamp": "ISO8601",
  "responses": {
    "PHQ2_Q1": {"value": 0-3, "text": "Not at all"},
    "PHQ2_Q2": {"value": 0-3, "text": "Several days"},
    "BPG_MH": {"value": 1-2, "text": "No"},
    "HTH_GEN": {"value": 1-5, "text": "Good"},
    "PRE_RX": {"value": 1-2, "text": "Yes"},
    "PRE_RX_MH": {"value": "Yes|No|Not sure", "text": "No"},
    "PRE_EXER": {"value": 1-2, "text": "Yes"},
    "PRE_DIET": {"value": 1-2, "text": "No"},
    "OWGT_OBS": {"value": 1-2, "text": "No"},
    "BPG_TALK": {"value": 1-2, "text": "Yes"},
    "FLU_SRC": {"value": 1-7, "text": "Family doctor"}
  },
  "calculated_scores": {
    "PHQ2_Total": 3,
    "High_Risk_Flags": 0,
    "Lifestyle_Risk": 1,
    "Final_Classification": "HIGH_RISK"
  },
  "routing": {
    "existing_provider": true,
    "care_setting": "Family doctor"
  }
}
```

---

## 🎨 UI/UX Recommendations

### Progress Indicator
Show user progress through the questionnaire:
```
Section 1: PHQ-2 Screening          [████████░░] 20%
Section 2: Mental Health History    [████████░░] 40%
Section 3: Health Status            [████████░░] 60%
Section 4: Lifestyle Factors        [████████░░] 80%
Section 5: Healthcare Access        [██████████] 100%
```

### Question Presentation
- **One question per screen** (mobile-friendly)
- **Large, tappable radio buttons**
- **Optional "Why we ask this" info icon** for each question
- **"Prefer not to answer" always available**
- **Back button enabled** (allow users to change previous answers)

### Privacy & Consent
- **HIPAA-compliant disclaimer** before starting
- **Data storage notice** (anonymous vs identifiable)
- **Option to download results** after completion

---

## ✅ Validation Rules

| Question | Required? | Validation |
|----------|-----------|------------|
| Q1-Q2 | Recommended | Allow skip with warning |
| Q3-Q8 | Optional | "Prefer not to answer" available |
| Q9-Q10 | Recommended | Needed for routing, but can skip |

**Minimum Required for Risk Classification**: PHQ-2 (Q1-Q2) only
- If user skips most questions, default to PHQ-2 score only
- Show warning: "More complete answers help us give better recommendations"

---

*This question flow is based on PRAMS Phase 8 data (N=178,299) and validated PHQ-2 screening guidelines.*
