# PRAMS Variable Categories Analysis

## Dataset Overview
- **File**: phase8_2016_2021_std_l.sas7bdat
- **Total Records**: 178,299
- **Note**: High percentage of missing values across all variables (70-97%)

---

## Variable Categories for Multiple-Choice Questions

### 1. **BPG_MH** - Pre-pregnancy counseling or treatment for mental health
**Label**: Pre-preg -- counseling or tx for MH (FORCED SKIP)
**Format**: NYS1F
**Codebook Values**: 1=NO, 2=YES, .B=DK/BLANK, .S=SKIP

| Value | Category | Count | Percentage |
|-------|----------|-------|------------|
| 1 | **No** | 9,901 | 5.55% |
| 2 | **Yes** ⚠️ | 3,873 | 2.17% |
| NA | Missing/Skipped | 164,525 | 92.27% |

**App Question**: *"Before you got pregnant, did you receive counseling or treatment from a health care worker for depression, anxiety, or other mental health conditions?"*
- [ ] Yes → **HIGH RISK** - Route to depression screener
- [ ] No
- [ ] Prefer not to answer

**Critical Finding**: 3,873 respondents (2.17%) reported receiving mental health treatment before pregnancy

---

### 2. **PRE_DEPR** - Pre-pregnancy check for depression/anxiety (CT only)
**Label**: Pre-pregnancy check for depression/anxiety
**Format**: NY1F
**Codebook Values**: 1=NO, 2=YES, .B=DK/BLANK
**Note**: This variable is only used by Connecticut and will only be available through a separate request to Connecticut

| Value | Category | Count | Percentage |
|-------|----------|-------|------------|
| NA | Missing (not available) | 178,299 | 100.00% |

**Status**: ⚠️ **NOT AVAILABLE** in this dataset - Connecticut-specific question only

---

### 3. **HTH_GEN** - General Health Status
**Label**: General Health
**Format**: HTH_GEN
**Codebook Values**: 1=EXCELLENT, 2=VERY GOOD, 3=GOOD, 4=FAIR, 5=POOR, .B=BLANK/DK

| Value | Category | Count | Percentage |
|-------|----------|-------|------------|
| 1 | **Excellent** | 6,387 | 3.58% |
| 2 | **Very Good** | 8,620 | 4.83% |
| 3 | **Good** | 6,585 | 3.69% |
| 4 | **Fair** ⚠️ | 1,705 | 0.96% |
| 5 | **Poor** ⚠️ | 167 | 0.09% |
| NA | Missing | 154,835 | 86.84% |

**App Question**: *"In general, how would you describe your health before you got pregnant?"*
- [ ] Excellent
- [ ] Very Good
- [ ] Good
- [ ] Fair → **Risk Amplifier** - Elevate urgency
- [ ] Poor → **Risk Amplifier** - Elevate urgency

**Risk Rule**: Fair/Poor (4 or 5) = Moderate→High Risk

---

### 4. **PRE_RX** - Pre-pregnancy prescription medications
**Label**: Pre-pregnancy prescrip meds
**Format**: NY1F
**Codebook Values**: 1=NO, 2=YES, .B=DK/BLANK

| Value | Category | Count | Percentage |
|-------|----------|-------|------------|
| 1 | **No** | 40,497 | 22.71% |
| 2 | **Yes** ⚠️ | 12,556 | 7.04% |
| NA | Missing | 125,246 | 70.24% |

**App Question Sequence**:
1. *"In the month before you got pregnant, were you taking any prescription medications?"*
   - [ ] Yes → **Follow-up required**
   - [ ] No
   - [ ] Prefer not to answer

2. **If Yes**: *"Were any of these medications for depression, anxiety, or other mental health conditions?"*
   - [ ] Yes → **HIGH RISK**
   - [ ] No
   - [ ] Unsure → **HIGH RISK** (treat conservatively)

---

### 5. **OWGT_OBS** - Health problem - overweight/obese
**Label**: Health problem - overweight/obese
**Format**: NY1F
**Codebook Values**: 1=NO, 2=YES, .B=DK/BLANK

| Value | Category | Count | Percentage |
|-------|----------|-------|------------|
| 1 | **No** | 5,539 | 3.11% |
| 2 | **Yes** ⚠️ | 2,786 | 1.56% |
| NA | Missing | 169,974 | 95.33% |

**App Question**: *"Before you got pregnant, did you have any of the following health problems: overweight or obesity?"*
- [ ] Yes → **Modest Risk Amplifier**
- [ ] No
- [ ] Prefer not to answer

**Risk Rule**: Use as modest modifier; combine with symptoms

---

### 6. **PRE_EXER** - Pre-pregnancy exercise 3+ days/week
**Label**: Pre-pregnancy exercise 3+ days/wk
**Format**: NY1F
**Codebook Values**: 1=NO, 2=YES, .B=DK/BLANK

| Value | Category | Count | Percentage |
|-------|----------|-------|------------|
| 1 | **No** ⚠️ | 31,671 | 17.76% |
| 2 | **Yes** | 21,407 | 12.01% |
| NA | Missing | 125,221 | 70.23% |

**App Question**: *"During the month before you got pregnant, did you exercise for at least 30 minutes on 3 or more days per week?"*
- [ ] Yes (Active) → Protective factor
- [ ] No (Inactive) → **Modest Risk Amplifier**
- [ ] Prefer not to answer

**Risk Rule**: "No exercise" (Value 1) modestly increases risk
**Finding**: 31,671 respondents (17.76%) reported no regular exercise

---

### 7. **PRE_DIET** - Pre-pregnancy dieting
**Label**: Pre-pregnancy dieting
**Format**: NY1F
**Codebook Values**: 1=NO, 2=YES, .B=DK/BLANK

| Value | Category | Count | Percentage |
|-------|----------|-------|------------|
| 1 | **No** | 38,303 | 21.48% |
| 2 | **Yes** ⚠️ | 14,817 | 8.31% |
| NA | Missing | 125,179 | 70.21% |

**App Question**: *"In the month before you got pregnant, were you trying to lose weight or control your weight by dieting?"*
- [ ] Yes → **Modest Risk Amplifier**
- [ ] No
- [ ] Prefer not to answer

**Risk Rule**: Dieting (Value 2) can modestly increase risk (body image concerns)
**Finding**: 14,817 respondents (8.31%) reported dieting before pregnancy

---

### 8. **BPG_TALK** - Healthcare worker discussed pregnancy preparation
**Label**: HCW discussed preparing for pregnancy
**Format**: NY1F
**Codebook Values**: 1=NO, 2=YES, .B=DK/BLANK

| Value | Category | Count | Percentage |
|-------|----------|-------|------------|
| 1 | **No** | 38,516 | 21.60% |
| 2 | **Yes** ✓ | 14,952 | 8.39% |
| NA | Missing | 124,831 | 70.01% |

**App Question**: *"Before you got pregnant, did a health care worker talk with you about preparing for pregnancy?"*
- [ ] Yes → **Existing clinical touchpoint** - Route to this system
- [ ] No
- [ ] Prefer not to answer

**Routing Logic**: If Yes (Value 2), user already has a healthcare connection; prioritize referral to their existing provider
**Finding**: 14,952 respondents (8.39%) had pregnancy preparation discussions with healthcare workers

---

### 9. **FLU_SRC** - Where flu shot was given
**Label**: Where flu shot was given (FORCED SKIP)
**Format**: FLU_SRC
**Codebook Values**: 1=OBGYN OFFICE, 2=FAMILY DR. OFFICE, 3=HEALTH DEPT./CLINIC, 4=HOSPITAL, 5=PHARMACY/STORE, 6=WORK/SCHOOL, 7=OTHER, .B=BLANK/DK, .S=SKIP

| Value | Category | Count | Percentage |
|-------|----------|-------|------------|
| 1 | **OB/Gyn office** | 1,899 | 1.07% |
| 2 | **Family doctor office** | 756 | 0.42% |
| 3 | **Health department/clinic** | 241 | 0.14% |
| 4 | **Hospital** | 745 | 0.42% |
| 5 | **Pharmacy/drug store** | 536 | 0.30% |
| 6 | **Work/school** | 379 | 0.21% |
| 7 | **Other** | 82 | 0.05% |
| NA | Missing/Skipped | 173,661 | 97.40% |

**App Question**: *"Where do you typically receive healthcare services? (Select the place you visit most often)"*
- [ ] OB/Gyn office → Route to local OB/Gyn with behavioral health
- [ ] Family doctor/PCP → Route to PCP with behavioral health
- [ ] Community health clinic → Route to public clinics + hotlines
- [ ] Hospital → Route to hospital-based behavioral health
- [ ] Pharmacy → Route to pharmacy with walk-in care + telehealth
- [ ] Work/school clinic
- [ ] Other
- [ ] I don't regularly visit any healthcare provider → Emphasize telehealth + crisis lines

**Routing Logic**: Match referral destination to user's familiar care setting

---

## Risk Scoring Summary

### High Risk Triggers (Any "Yes" → High Risk)
1. **BPG_MH = Yes** (prior mental health treatment)
2. **PRE_RX = Yes** + medication was for mood/anxiety
3. **HTH_GEN = Fair/Poor** (4 or 5)
4. **Positive symptom gate** (PHQ-2 ≥ 2)

### Moderate Risk Modifiers
- Multiple lifestyle factors: No exercise + Dieting + Overweight

### Routing Enhancers
- **BPG_TALK = Yes** → Route to existing provider first
- **FLU_SRC** → Match referral to familiar care setting

---

## Implementation Notes

### Missing Data Strategy
- **70-97% missing**: Most variables have very high missing rates
- **Approach**: Make all questions optional with "Prefer not to answer"
- **Design**: Progressive disclosure - only ask follow-ups when relevant
- **PRE_DEPR**: Skip entirely (100% missing in this dataset)

### Question Flow Optimization
1. **Start with symptom gate** (PHQ-2) - 2 questions
2. **Ask critical risk factors**:
   - BPG_MH (prior MH treatment)
   - HTH_GEN (general health)
   - PRE_RX + follow-up (medications)
3. **Add lifestyle context** (optional):
   - PRE_EXER, PRE_DIET, OWGT_OBS
4. **Gather routing info**:
   - BPG_TALK (existing provider?)
   - FLU_SRC proxy (usual care setting)

### Skip Logic
- If **BPG_MH = Yes**: Immediately flag as High Risk, still collect other data for context
- If **PRE_RX = No**: Skip medication follow-up
- If **HTH_GEN = Excellent/Very Good/Good**: Don't emphasize health status in triage

---

## Next Steps for App Development

1. **Validate Format Assumptions**: Confirm category labels with PRAMS codebook
2. **Design UI/UX**: Create intuitive multiple-choice questions
3. **Build Risk Algorithm**: Implement scoring logic based on responses
4. **Create Referral Database**: Map FLU_SRC categories to local resources
5. **Test with Users**: Pilot test question flow and clarity

