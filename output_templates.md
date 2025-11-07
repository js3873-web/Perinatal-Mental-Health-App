# Mental Health Screening App - Output Templates

## Overview
Two-tier output system with four components:
1. **Risk Score/Category** - Clear classification and explanation
2. **Provider Referrals** - Personalized based on user's care setting
3. **Self-Help Resources** - Education and coping strategies
4. **Crisis Resources** - Emergency contacts and hotlines

---

# 🟢 LOW RISK OUTPUT

---

## 1. Risk Score/Category Display

### Primary Message
```
✓ Your Results: Low Risk

Based on your responses, you are currently at LOW RISK for perinatal
depression or anxiety. This is good news!

Your Scores:
• Depression screening (PHQ-2): [X]/6 - Negative
• Mental health history: No concerning factors
• Lifestyle factors: [X]/3 risk factors present

What this means:
You're showing minimal or no symptoms of depression right now. However,
it's important to monitor your mood throughout pregnancy and after delivery,
as perinatal mood changes can happen at any time.
```

### Detailed Breakdown (Expandable)
```
Your Response Summary:

✓ Mood & Interest
  Over the past 2 weeks, you reported [low/minimal] feelings of depression
  or loss of interest in activities. This is a positive sign.

✓ Mental Health History
  You [have not received / did not report] prior mental health treatment.

✓ General Health
  You described your pre-pregnancy health as [Excellent/Very Good/Good].

✓ Lifestyle Factors
  [Dynamic text based on responses]
  • Exercise: You [did/did not] exercise regularly
  • Diet: You [were/were not] actively dieting
  • Weight: You [did/did not] report concerns about weight

Next Steps:
Continue monitoring your mental health and consider the self-care
recommendations below. Re-screen in 2 weeks or if you notice changes
in your mood.
```

---

## 2. Provider Referrals (Low Risk - Preventive Care)

### If User Has Existing Provider (BPG_TALK = Yes)
```
📋 Your Healthcare Team

You mentioned that a healthcare worker discussed pregnancy preparation
with you before. This is great! Continue working with your existing
provider for routine prenatal care.

Routine Check-in Recommendation:
During your next prenatal appointment, mention that you completed this
mental health screening. Your provider can:
• Monitor your mental health throughout pregnancy
• Provide resources if you notice mood changes
• Connect you to support services if needed

Your Usual Care Setting: [FLU_SRC response]
```

### If User Has NO Existing Provider (BPG_TALK = No)
**Dynamic routing based on FLU_SRC response:**

#### Option A: OB/Gyn Office
```
🏥 Recommended Next Steps

You typically receive care at an OB/Gyn office. We recommend:

1. Schedule a prenatal care appointment if you haven't already
2. Discuss mental health monitoring with your OB/Gyn
3. Ask about integrated behavioral health services at the practice

Many OB/Gyn offices now offer mental health screening and support
as part of routine prenatal care.

[Button: Find OB/Gyn Near Me]
```

#### Option B: Family Doctor / Primary Care
```
🏥 Recommended Next Steps

You typically receive care through a family doctor. We recommend:

1. Schedule a prenatal care appointment with your PCP
2. Ask for a referral to an OB/Gyn if needed
3. Discuss mental health monitoring during your visit

Your primary care doctor can coordinate your prenatal care and
provide ongoing mental health monitoring.

[Button: Contact My Doctor]
```

#### Option C: Community Health Clinic
```
🏥 Recommended Next Steps

You typically receive care at a community health clinic. We recommend:

1. Visit your local health department or community clinic for
   prenatal care
2. Ask about free or low-cost mental health services
3. Inquire about WIC, social services, and support groups

Community health centers often offer comprehensive services including
prenatal care, mental health support, and social services.

[Button: Find Community Clinic Near Me]
```

#### Option D: Hospital
```
🏥 Recommended Next Steps

You typically receive care at a hospital. We recommend:

1. Contact the hospital's OB/Gyn department for prenatal care
2. Ask about hospital-based mental health services
3. Inquire about prenatal classes and support groups

Hospital systems often have comprehensive maternal health programs
with integrated mental health services.

[Button: Find Hospital Maternal Health Services]
```

#### Option E: Pharmacy
```
🏥 Recommended Next Steps

You mentioned you typically go to pharmacies for healthcare. For
pregnancy care, you'll need:

1. An OB/Gyn or prenatal care provider for your pregnancy
2. We can help you find affordable options nearby
3. Some pharmacies offer MinuteClinic services for initial
   consultations

Consider also: Telehealth options for mental health support

[Button: Find Prenatal Care Provider]
[Button: Explore Telehealth Options]
```

#### Option F: Work/School Clinic
```
🏥 Recommended Next Steps

You typically use your work or school health clinic. For pregnancy:

1. Ask if your work/school clinic offers prenatal care referrals
2. Check if your insurance covers OB/Gyn services
3. Consider using your Employee Assistance Program (EAP) if
   available for mental health support

[Button: Learn About EAP]
[Button: Find OB/Gyn]
```

#### Option G: No Regular Provider
```
🏥 Recommended Next Steps

We noticed you don't regularly visit a healthcare provider. For
your pregnancy, it's important to establish prenatal care.
We can help you find:

1. Low-cost or free prenatal care clinics
2. Telehealth options for remote consultations
3. Community resources and support programs

You have options regardless of insurance status.

[Button: Find Low-Cost Care Options]
[Button: Explore Telehealth]
[Button: Learn About Medicaid Pregnancy Coverage]
```

---

## 3. Self-Help Resources (Low Risk - Prevention & Education)

```
📚 Mental Health Resources for You

Education & Information
─────────────────────────
• Understanding Perinatal Mood Changes
  Learn about normal emotional changes during pregnancy and
  warning signs to watch for.
  [Link: Educational Article]

• Building Resilience During Pregnancy
  Evidence-based strategies for maintaining mental wellness.
  [Link: Interactive Guide]

• Partners & Support People: How to Help
  Resource for partners, family, and friends.
  [Link: Support Guide]

Self-Care Strategies
─────────────────────────
✓ Stay Active
  Regular exercise (even 10-15 minutes daily) can boost mood
  and reduce stress. Safe pregnancy exercises: walking,
  prenatal yoga, swimming.
  [Link: Safe Exercise Guide]

✓ Connect with Others
  Join a prenatal support group or connect with other expecting
  parents. Social support is protective against depression.
  [Button: Find Support Groups Near Me]

✓ Prioritize Sleep
  Aim for 7-9 hours per night. Good sleep hygiene helps
  regulate mood.
  [Link: Sleep Tips for Pregnancy]

✓ Practice Mindfulness
  Simple breathing exercises and meditation can reduce anxiety.
  [Button: Try a 5-Minute Guided Meditation]

✓ Maintain Nutrition
  Balanced diet with omega-3s may support mental health.
  [Link: Nutrition Guide for Pregnancy]

Mobile Apps (Evidence-Based)
─────────────────────────────
• Calm - Meditation and relaxation
• Headspace - Mindfulness for pregnancy
• Expectful - Prenatal meditation and hypnotherapy
• What to Expect - Pregnancy tracking with wellness tips

Community Resources
─────────────────────────
• Local prenatal yoga classes
• Pregnancy support groups
• Online communities (e.g., WhatToExpect forums, BabyCenter)
• Faith-based support (if applicable)

[Button: Save Resources to My Phone]
[Button: Share Resources with Partner]
```

---

## 4. Crisis Resources (Always Included - All Risk Levels)

```
🆘 If You Need Immediate Help

If you or someone you know is in crisis, help is available 24/7:

Emergency Resources
─────────────────────────
🚨 If life-threatening emergency: Call 911

📞 National Suicide Prevention Lifeline
   988 or 1-800-273-8255 (TALK)
   24/7, free, confidential
   [Button: Call Now]
   [Button: Chat Online]

📱 Crisis Text Line
   Text HOME to 741741
   24/7 crisis support via text
   [Button: Start Text Chat]

🤰 Postpartum Support International Helpline
   1-800-944-4773 (4PPD)
   English & Español
   [Button: Call PSI Helpline]
   Text in English: 800-944-4773
   Text en Español: 971-203-7773

Additional Support
─────────────────────────
• National Maternal Mental Health Hotline
  1-833-TLC-MAMA (1-833-852-6262)
  24/7, free, confidential support for pregnant and
  postpartum individuals

• SAMHSA National Helpline
  1-800-662-4357 (HELP)
  Treatment referral and information service

Warning Signs - Seek Help If You Experience:
• Thoughts of harming yourself or your baby
• Severe anxiety or panic attacks
• Inability to care for yourself or your baby
• Hallucinations or hearing voices
• Rapid mood swings or manic behavior
• Intrusive, frightening thoughts

[Button: Safety Plan] [Button: Find Emergency Care]
```

---

# 🔴 HIGH RISK OUTPUT

---

## 1. Risk Score/Category Display

### Primary Message
```
⚠️ Your Results: High Risk - Action Recommended

Based on your responses, you are currently at HIGH RISK for perinatal
depression or anxiety. This is important information, and we want to
help you get the support you need.

Your Scores:
• Depression screening (PHQ-2): [X]/6 [if ≥3: "- Positive screen"]
• Mental health risk factors: [X] present
• Lifestyle factors: [X]/3 risk factors present

Classification Reason: [Dynamic based on which rule triggered]
[Rule 1: "Your depression screening suggests you may be experiencing
         symptoms of depression"]
[Rule 2: "Your mental health history indicates increased risk"]
[Rule 3: "Combination of symptoms and multiple risk factors"]

What this means:
You may be experiencing or at increased risk for depression or
anxiety during your pregnancy. This is COMMON (affects 15-20% of
pregnant people) and TREATABLE. The most important step is to
connect with a healthcare provider who can provide proper evaluation
and support.
```

### Detailed Breakdown (Expandable)
```
Your Response Summary:

⚠️ Mood & Interest
  Over the past 2 weeks, you reported [moderate/significant] feelings
  of depression or loss of interest in activities. These symptoms
  warrant further evaluation.
  [If PHQ-2 ≥3: "Your screening score suggests you may be experiencing
                 clinical depression."]

[If BPG_MH=Yes:]
⚠️ Mental Health History
  You previously received mental health treatment before pregnancy.
  This is an important risk factor for perinatal depression. Having
  a history of depression increases the likelihood of recurrence
  during pregnancy.

[If PRE_RX_MH=Yes:]
⚠️ Medications
  You were taking medications for depression or anxiety before
  pregnancy. It's important to discuss with your provider whether
  to continue, adjust, or change your medications during pregnancy.

[If HTH_GEN=Fair/Poor:]
⚠️ General Health
  You described your pre-pregnancy health as [Fair/Poor]. Poor
  physical health is associated with increased depression risk.

[If Lifestyle_Risk ≥2:]
⚠️ Lifestyle Factors
  You reported multiple lifestyle factors that may affect mental
  health:
  [List specific factors: no exercise, dieting, weight concerns]

Immediate Next Steps:
1. Contact a healthcare provider within 24-48 hours
2. Complete a full depression assessment (we can help)
3. Review crisis resources below (available 24/7)
4. Consider sharing these results with a trusted support person
```

---

## 2. Provider Referrals (High Risk - Urgent Care)

### Urgency Banner (Always Displayed)
```
🚨 IMPORTANT: Early intervention is most effective

Research shows that treating perinatal depression early leads to
better outcomes for both you and your baby. Please contact a
provider within the next 24-48 hours.
```

### If User Has Existing Provider (BPG_TALK = Yes)
```
📋 Contact Your Healthcare Provider - Priority

You mentioned you've worked with a healthcare provider before.
This is your best starting point.

Immediate Action Steps:
─────────────────────────
1. ☎️ Call your provider's office TODAY
   Say: "I completed a mental health screening that showed I'm
        at high risk for perinatal depression. I need to speak
        with my provider as soon as possible."

2. 📅 Request an urgent appointment (within 24-48 hours)
   If they can't see you today/tomorrow, ask:
   • Is there a same-day appointment available?
   • Can I speak with a nurse or care manager now?
   • Is there a mental health specialist in the practice?

3. 📋 Bring your screening results
   [Button: Download My Results] [Button: Email Results to Provider]

Your Usual Care Setting: [FLU_SRC response]

If you can't reach your provider or need help sooner:
[Button: Find Immediate Mental Health Services]
[Button: Call Crisis Hotline]

Alternative Options:
• Telehealth mental health appointment (same-day often available)
• Hospital emergency department (if in crisis)
• Community mental health center walk-in services
```

### If User Has NO Existing Provider (BPG_TALK = No)
**Dynamic routing based on FLU_SRC response:**

#### Option A: OB/Gyn Office
```
🏥 Find Mental Health Support Through OB/Gyn Care

You typically receive care at an OB/Gyn office. Many OB/Gyn
practices have integrated behavioral health services.

Immediate Action Steps:
─────────────────────────
1. Call an OB/Gyn office WITHIN 24 HOURS
   Script: "I'm pregnant and recently screened positive for depression.
           I need an urgent appointment with a provider who can help
           with both prenatal care and mental health."

2. What to ask:
   ✓ Do you have a psychiatrist or therapist on staff?
   ✓ Can you refer me to perinatal mental health specialists?
   ✓ Do you accept my insurance / offer sliding scale fees?
   ✓ Are same-day or next-day appointments available?

3. If they can't see you quickly:
   ✓ Ask for a warm referral to a mental health provider
   ✓ Request a temporary therapist while you wait for an appointment

[Button: Find OB/Gyn with Behavioral Health Near Me]
[Button: Schedule Telehealth OB Appointment Today]

Alternative Fast Options:
• Perinatal Psychiatry Telehealth - Same-day appointments often available
• Community Mental Health Center - Walk-in services
• Hospital OB/Emergency Dept - If symptoms are severe
```

#### Option B: Family Doctor / Primary Care
```
🏥 Find Mental Health Support Through Primary Care

You typically see a family doctor. Primary care physicians can
treat perinatal depression or refer to specialists.

Immediate Action Steps:
─────────────────────────
1. Call your family doctor's office TODAY
   Script: "I'm pregnant and screened positive for depression. I need
           an urgent mental health evaluation and want to discuss
           treatment options."

2. What to ask:
   ✓ Can my PCP treat perinatal depression?
   ✓ Do you have behavioral health consultants in the practice?
   ✓ Can you refer me to a perinatal psychiatrist or therapist?
   ✓ Are medication adjustments something you can help with?

3. Your doctor can provide:
   ✓ Full depression assessment (PHQ-9 or EPDS)
   ✓ Medication management (if appropriate)
   ✓ Referral to therapist or psychiatrist
   ✓ Coordination with your prenatal care

[Button: Contact My Family Doctor]
[Button: Find PCP with MH Services Near Me]

If your PCP can't see you quickly:
[Button: Find Same-Day Telehealth Mental Health]
[Button: Locate Community Mental Health Center]
```

#### Option C: Community Health Clinic
```
🏥 Find Mental Health Support at Community Clinics

You typically use community health clinics. These centers often
provide integrated mental health and prenatal care services,
often on a sliding scale based on income.

Immediate Action Steps:
─────────────────────────
1. Contact your local health department or FQHC TODAY
   Federally Qualified Health Centers (FQHCs) serve all patients
   regardless of insurance or ability to pay.

2. Services often available:
   ✓ Integrated behavioral health (therapists on-site)
   ✓ Prenatal care + mental health together
   ✓ Medication management (psychiatry)
   ✓ Care coordination and social services
   ✓ Connection to WIC, housing, and other supports

3. What to say when calling:
   "I'm pregnant and screened high-risk for depression. I need
   urgent mental health services and prenatal care. Do you have
   same-day or walk-in appointments?"

[Button: Find FQHC Near Me]
[Button: Locate Health Department Mental Health Services]

Additional Resources:
• Many clinics offer walk-in hours (mornings usually best)
• If no immediate appointments, ask about crisis services
• Request a care manager to help navigate the system

National Resources:
• HRSA Health Center Locator: findahealthcenter.hrsa.gov
• National Association of Community Health Centers: nachc.org
```

#### Option D: Hospital
```
🏥 Find Mental Health Support Through Hospital Services

You typically receive care at hospitals. Hospital systems often
have specialized perinatal psychiatry programs.

Immediate Action Steps:
─────────────────────────
1. Contact the hospital's maternal mental health program
   Many hospitals now have dedicated perinatal psychiatry services.
   Call the main number and ask for:
   • "Maternal mental health services"
   • "Perinatal psychiatry"
   • "OB/Gyn behavioral health"

2. Services typically offered:
   ✓ Perinatal psychiatry (medication management)
   ✓ Individual therapy
   ✓ Group therapy for pregnant/postpartum people
   ✓ Intensive outpatient programs (if needed)

3. When to go to Emergency Department:
   • If you have thoughts of harming yourself or baby
   • If symptoms are severe and you can't wait for an appointment
   • If you're experiencing panic attacks or severe anxiety

[Button: Find Hospital Perinatal Mental Health Program]
[Button: Locate Hospital Behavioral Health Services]

Major hospital systems with perinatal psychiatry:
• Teaching hospitals / University medical centers
• Large health systems (often have specialty programs)

If the hospital doesn't have a program:
[Button: Find Perinatal Psychiatrist Near Me]
[Button: Telehealth Perinatal Mental Health]
```

#### Option E: Pharmacy
```
🏥 Find Mental Health Support - Urgent Referral Needed

You mentioned you typically go to pharmacies for healthcare. For
mental health support during pregnancy, you'll need specialized care.

We can help you access care QUICKLY:

Immediate Options (Available Today):
─────────────────────────────
1. 📱 Telehealth Mental Health (FASTEST)
   Same-day video appointments with psychiatrists and therapists
   who specialize in pregnancy-related depression.

   • Talkspace - Perinatal specialists available
   • BetterHelp - Can match with perinatal therapist
   • MDLive / Teladoc - Psychiatry consults same-day
   • Maven Clinic - Perinatal mental health platform

   [Button: Find Telehealth Provider]

2. 🏥 Community Mental Health Center
   Walk-in services often available, sliding scale fees

   [Button: Find Community Mental Health Near Me]

3. ☎️ Crisis Services (24/7)
   Talk to a counselor NOW if you need immediate support

   [Button: Call/Text Crisis Line]

For Ongoing Prenatal Care:
You'll also need an OB/Gyn or midwife for your pregnancy. We can help
you find affordable options.

[Button: Find Prenatal Care Provider]

Some pharmacies (CVS MinuteClinic, Walgreens Healthcare Clinic) can
provide initial consultation and referrals - visit in person if available.
```

#### Option F: Work/School Clinic
```
🏥 Find Mental Health Support - Employee/Student Resources

You typically use your work or school health clinic. You likely have
additional mental health benefits available to you.

Immediate Action Steps:
─────────────────────────
1. 🏢 Check Your Employee Assistance Program (EAP)
   If you have a job, you likely have free EAP benefits:
   • Typically 3-8 FREE therapy sessions
   • Can get same-day or next-day appointments
   • Confidential (employer doesn't know)
   • Can help find ongoing care after EAP sessions

   Where to find EAP info:
   ✓ HR department / employee handbook
   ✓ Back of your insurance card
   ✓ Your company intranet / benefits portal

   [Button: Learn More About EAP]

2. 🎓 Student Health Services (if in school)
   College/university health centers often have:
   • Free or low-cost counseling
   • Psychiatry services
   • Same-day crisis appointments
   • Referrals to specialized perinatal providers

   [Button: Contact Student Health Services]

3. 🏥 Your Health Insurance
   Call the number on your insurance card and say:
   "I'm pregnant and screened positive for depression. I need
   urgent referral to a perinatal mental health provider."

   Ask for:
   ✓ Perinatal psychiatrists in-network
   ✓ Therapists who specialize in pregnancy/postpartum
   ✓ Whether they have a behavioral health nurse line

   [Button: Find In-Network Mental Health Provider]

Fast Telehealth Options:
Many EAPs and insurance plans now cover telehealth mental health.
This is often the quickest way to see someone.

[Button: Find Telehealth Mental Health Today]
```

#### Option G: No Regular Provider
```
🏥 Find Mental Health Support - We'll Help You Navigate

We noticed you don't regularly visit a healthcare provider.
That's okay - we'll help you find the right support, regardless
of your insurance or financial situation.

Fastest Options (Available Within 24-48 Hours):
─────────────────────────────────────────────

1. 📱 Telehealth Mental Health (RECOMMENDED - Quick & Easy)
   Video appointments available TODAY with perinatal specialists.
   Many offer sliding scale fees or accept Medicaid.

   Perinatal-Focused Platforms:
   • Postpartum Support International Provider Directory
   • Maven Clinic - Perinatal mental health specialists
   • Talkspace / BetterHelp - Can match with perinatal therapist

   [Button: Find Telehealth Provider Now]

2. 🏥 Community Mental Health Center (Low/No Cost)
   Federally Qualified Health Centers (FQHCs) serve everyone:
   • No insurance needed
   • Sliding scale fees based on income
   • Walk-in services often available
   • Can provide prenatal care + mental health together

   [Button: Find FQHC Near Me]

3. ☎️ Call a Perinatal Mental Health Warmline
   Talk to a trained counselor who can help you find local services:

   • Postpartum Support International: 1-800-944-4773
   • National Maternal Mental Health Hotline: 1-833-TLC-MAMA

   [Button: Call Warmline for Help]

Financial Assistance Options:
─────────────────────────────
• Medicaid Pregnancy Coverage: Available in all states, covers
  mental health treatment. Apply even if you were previously denied.
  [Button: Apply for Medicaid]

• Sliding Scale Therapy: Many therapists offer reduced fees
  [Button: Find Sliding Scale Providers]

• Free Support Groups: Peer support can be very helpful
  [Button: Find Free Support Groups]

Hospital Emergency Resources:
If you're in crisis or symptoms are severe, go to any hospital
emergency department. They must evaluate you regardless of insurance.

[Button: Find Nearest Hospital Emergency Dept]
```

---

## 3. Self-Help Resources (High Risk - Supportive, Not Replacement for Care)

```
🧰 Additional Support Tools

⚠️ IMPORTANT: These resources support professional treatment but
do not replace it. Please contact a healthcare provider as soon as possible.

Immediate Symptom Management
─────────────────────────────
While you're waiting for your appointment, these strategies may
help manage symptoms:

• Breathing Exercises for Anxiety
  5-4-3-2-1 grounding technique
  [Button: Try Now - 3 minutes]

• Sleep Hygiene Tips
  Depression worsens with poor sleep
  [Link: Sleep Strategies]

• Crisis Coping Skills
  What to do when symptoms feel overwhelming
  [Button: View Coping Plan]

• Reach Out to Support Person
  Share your screening results with a trusted friend, partner, or
  family member. You don't have to go through this alone.
  [Button: Share Results]

Structured Self-Help Programs
─────────────────────────────
Evidence-based online programs (complement professional care):

• MoodGYM - Cognitive behavioral therapy program
• This Way Up - CBT for depression and anxiety
• SuperBetter - Build resilience through gaming

Educational Resources
─────────────────────────────
• "What is Perinatal Depression?" - Video (8 min)
  [Link: Watch Video]

• "Treatment Options Explained"
  Understanding therapy, medication, and combined approaches
  [Link: Read Guide]

• "Talking to Your Partner About Mental Health"
  Communication strategies and what support looks like
  [Link: Partner Guide]

Support Groups (Peer Support)
─────────────────────────────
Connecting with others who understand can be powerful:

• Postpartum Support International Groups
  Virtual and in-person meetings
  [Button: Find Support Group]

• Online Communities
  • PSI Chat (monitored by trained volunteers)
  • r/PregnancyAfterLoss (Reddit)
  • Expecting with Depression (Facebook group)

Safety Planning
─────────────────────────────
If you're having thoughts of self-harm:

• Create a safety plan with specific steps
• Identify warning signs
• List people to contact
• Remove access to means of harm
• Reasons for living

[Button: Create My Safety Plan] [Button: Download Safety Plan Template]

Medication Information
─────────────────────────────
If your provider recommends medication, you may have questions:

• "Antidepressants During Pregnancy: Safety Info"
  Evidence-based information about SSRIs and pregnancy
  [Link: Read More]

• MGH Center for Women's Mental Health
  Comprehensive research-based resources
  [Link: Visit Resource Center]
```

---

## 4. Crisis Resources (Emphasized for High Risk)

```
🆘 IMMEDIATE HELP AVAILABLE 24/7

If you're in crisis or having thoughts of harming yourself or your
baby, reach out NOW. Help is available immediately.

🚨 EMERGENCY (Life-Threatening)
─────────────────────────────
If you or your baby are in immediate danger:

CALL 911 or go to nearest Emergency Department

📞 CRISIS HOTLINES (Available Now)
─────────────────────────────────
All services are FREE, CONFIDENTIAL, and available 24/7:

🌟 National Suicide Prevention Lifeline
   988 or 1-800-273-8255
   24/7 crisis counseling
   [Button: CALL NOW] [Button: CHAT ONLINE]

📱 Crisis Text Line
   Text HOME to 741741
   24/7 support via text message
   [Button: START TEXT CHAT]

🤰 Postpartum Support International Helpline
   1-800-944-4773 (1-800-944-4PPD)
   Perinatal mental health specialists
   [Button: CALL PSI]

   Text Support:
   • English: Text 800-944-4773
   • Español: Text 971-203-7773

🆕 National Maternal Mental Health Hotline
   1-833-TLC-MAMA (1-833-852-6262)
   24/7 support specifically for pregnant and new parents
   Available in English and Spanish
   [Button: CALL HOTLINE]

📞 SAMHSA National Helpline
   1-800-662-HELP (4357)
   Treatment referral and information
   [Button: CALL SAMHSA]

When to Seek Immediate Help:
────────────────────────────
Contact emergency services or crisis hotline if you experience:

⚠️ Thoughts of harming yourself or ending your life
⚠️ Thoughts of harming your baby
⚠️ Severe, uncontrollable anxiety or panic
⚠️ Inability to eat, sleep, or care for yourself
⚠️ Hearing voices or seeing things that aren't there
⚠️ Intrusive, frightening thoughts you can't control
⚠️ Feeling detached from reality
⚠️ Severe rage or thoughts of violence

Hospital Emergency Departments
────────────────────────────
Any hospital ER can evaluate you for psychiatric emergencies.
You WILL be seen regardless of insurance or ability to pay.

What to expect:
• Crisis counselor will talk with you
• Psychiatric evaluation by MD or advanced practice nurse
• Safety plan and immediate treatment
• Referral to outpatient care
• Possible short-term hospitalization if needed (rare, only if necessary for safety)

[Button: Find Nearest Emergency Department]

Mobile Crisis Teams
───────────────────
Some areas have mobile crisis teams that can come to you.
These are alternatives to the ER when you need urgent help but
not necessarily hospitalization.

[Button: Find Mobile Crisis Services in My Area]

For Your Support People
───────────────────────
If someone you know is in crisis:
• Take all talk of suicide seriously
• Don't leave them alone
• Remove access to weapons, medications, or other means of harm
• Call crisis hotline or 911
• Stay calm and listen without judgment
• Help them get to treatment

[Link: Complete Guide for Support People]

Safety Planning Resources
──────────────────────────
• MY3 App - Crisis support app
  Keep crisis contacts, warning signs, and coping strategies
  on your phone
  [Button: Download MY3 App]

• Safety Plan Template
  Work through this with a counselor or trusted person
  [Button: Download Template]

🔒 All Crisis Services Are:
✓ FREE
✓ CONFIDENTIAL
✓ AVAILABLE 24/7/365
✓ No judgment, just support
✓ Can be anonymous if you prefer

Remember: Reaching out for help is a sign of strength, not weakness.
You deserve support, and recovery is possible.
```

---

## 📊 Results Summary (Optional Email/PDF)

### Template for Downloadable Results

```
Mental Health Screening Results
[Date]

─────────────────────────────
RISK CLASSIFICATION: [LOW RISK / HIGH RISK]
─────────────────────────────

YOUR SCORES:

Depression Screening (PHQ-2): [X]/6
• Question 1 (Depressed Mood): [Score] - [Response text]
• Question 2 (Loss of Interest): [Score] - [Response text]

Mental Health History:
• Prior treatment before pregnancy: [Yes/No]
• Medications for mood/anxiety: [Yes/No/Not applicable]
• General health status: [Response]

Lifestyle Factors ([X]/3 present):
• Regular exercise (3+ days/week): [Yes/No]
• Dieting behavior: [Yes/No]
• Overweight/obesity concern: [Yes/No]

Healthcare Access:
• Existing provider relationship: [Yes/No]
• Typical care setting: [Response]

─────────────────────────────
RECOMMENDED NEXT STEPS:
─────────────────────────────

[LOW RISK:]
✓ Continue self-monitoring
✓ Discuss mental health with prenatal care provider
✓ Re-screen in 2-4 weeks or if symptoms change
✓ Use self-help resources
✓ Practice preventive self-care

[HIGH RISK:]
⚠️ Contact healthcare provider within 24-48 hours
⚠️ Complete full depression assessment (PHQ-9 or EPDS)
⚠️ Consider therapy and/or medication evaluation
⚠️ Use crisis resources if symptoms worsen
⚠️ Share results with support person

RESOURCES:

Crisis Hotlines (24/7):
• National Suicide Prevention Lifeline: 988
• PSI Helpline: 1-800-944-4773
• National Maternal MH Hotline: 1-833-TLC-MAMA

[Personalized provider referrals based on FLU_SRC]

Educational Resources:
• [Links to resources]

─────────────────────────────
DISCLAIMER:
─────────────────────────────
This screening is for informational purposes only and does not
constitute a clinical diagnosis. Results should be discussed with
a qualified healthcare provider. If you are experiencing a mental
health emergency, call 988 or 911 immediately.

Screening based on:
• Patient Health Questionnaire-2 (PHQ-2)
• PRAMS Phase 8 risk factors (2016-2021, N=178,299)
• Evidence-based perinatal mental health guidelines

Generated by: [App Name]
Support: [Contact information]

─────────────────────────────

[Button: Schedule Follow-up Appointment]
[Button: Save to Phone] [Button: Email to Provider]
[Button: Share with Support Person]
```

---

## 🎨 UI/UX Design Notes

### Color Coding
- **Low Risk**: Green accents (#28a745)
- **High Risk**: Red/Orange accents (#dc3545 / #fd7e14)
- Always use accessible color contrast ratios

### Tone & Language
- **Low Risk**: Positive, encouraging, preventive
- **High Risk**: Urgent but not alarming, hopeful, action-oriented

### Key Principles
1. **Clarity**: Use simple language, avoid medical jargon
2. **Actionability**: Every output should have clear next steps
3. **Empowerment**: Frame as "you have options" not "you're broken"
4. **Hope**: Emphasize that help is available and recovery is possible
5. **Accessibility**: Include audio options, large text, screen reader compatible

### Call-to-Action Buttons
- Make buttons large and clear
- Use action verbs: "Call Now", "Find Help", "Download Results"
- High-contrast colors
- Mobile-friendly (thumb-sized tap targets)

---

*These templates are designed for empathy, clarity, and actionability. All content is based on evidence-based practices for perinatal mental health screening and intervention.*
