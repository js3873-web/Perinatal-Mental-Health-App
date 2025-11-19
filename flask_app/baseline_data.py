"""
Baseline data from PRAMS Phase 8 (2016-2021)
NON-MISSING RESPONSES ONLY
Source: variable_categories_analysis.md
"""

BASELINE_DATA = {
    'dataset_info': 'PRAMS Phase 8 (2016-2021) - Non-missing responses only',

    # Total non-missing responses per variable
    'total_non_missing': {
        'BPG_MH': 13774,      # 9,901 + 3,873
        'HTH_GEN': 23464,     # 6,387 + 8,620 + 6,585 + 1,705 + 167
        'PRE_RX': 53053,      # 40,497 + 12,556
        'PRE_EXER': 53078,    # 31,671 + 21,407
        'PRE_DIET': 53120,    # 38,303 + 14,817
        'OWGT_OBS': 8325,     # 5,539 + 2,786
        'BPG_TALK': 53468,    # 38,516 + 14,952
        'FLU_SRC': 4638       # 1,899 + 756 + 241 + 745 + 536 + 379 + 82
    },

    # Risk factors from non-missing responses
    'risk_factors': {
        'prior_mh': 3873,           # BPG_MH = Yes
        'poor_health': 1872,        # HTH_GEN = Fair (1,705) + Poor (167)
        'no_exercise': 31671,       # PRE_EXER = No
        'dieting': 14817,           # PRE_DIET = Yes
        'overweight': 2786,         # OWGT_OBS = Yes
        'mh_meds': 0                # Not directly measured, will be from new responses
    },

    # Care settings from non-missing FLU_SRC responses
    'care_settings': {
        'OB/Gyn office': 1899,
        'Family doctor / Primary care physician': 756,
        'Community health clinic': 241,
        'Hospital': 745,
        'Pharmacy': 536,
        'Work or school clinic': 379,
        'Other': 82
    },

    # PHQ-2 estimates based on literature (10-12% positive rate)
    # Using total non-missing estimate of ~53,000 responses (average across variables)
    'phq2_distribution': {
        0: 15900,  # ~30%
        1: 13250,  # ~25%
        2: 12190,  # ~23%
        3: 5300,   # ~10%
        4: 3180,   # ~6%
        5: 2120,   # ~4%
        6: 1060    # ~2%
    },

    # Estimated risk classification
    # Assuming ~18% HIGH_RISK based on risk factors
    'risk_distribution': {
        'HIGH_RISK': 9540,   # ~18% of 53,000
        'LOW_RISK': 43460    # ~82% of 53,000
    }
}


def get_baseline_analytics():
    """
    Return baseline data in API format (counts only, no missing data)
    """
    return {
        'total_responses': 53000,  # Average non-missing responses
        'risk_distribution': BASELINE_DATA['risk_distribution'].copy(),
        'phq2_distribution': BASELINE_DATA['phq2_distribution'].copy(),
        'risk_factors': BASELINE_DATA['risk_factors'].copy(),
        'care_settings': BASELINE_DATA['care_settings'].copy()
    }


def merge_with_new_responses(new_responses):
    """
    Merge baseline data with new screening responses
    Only counts non-missing data
    """
    baseline = get_baseline_analytics()

    if not new_responses or len(new_responses) == 0:
        return baseline

    # Add count of new responses
    baseline['total_responses'] += len(new_responses)

    # Merge risk distributions
    for response in new_responses:
        risk_class = response.get('risk_result', {}).get('classification')
        if risk_class in ['HIGH_RISK', 'LOW_RISK']:
            baseline['risk_distribution'][risk_class] = \
                baseline['risk_distribution'].get(risk_class, 0) + 1

    # Merge PHQ-2 scores
    for response in new_responses:
        phq2_score = response.get('risk_result', {}).get('phq2_total')
        if phq2_score is not None and 0 <= phq2_score <= 6:
            baseline['phq2_distribution'][phq2_score] = \
                baseline['phq2_distribution'].get(phq2_score, 0) + 1

    # Merge risk factors (only count non-missing/non-NA responses)
    for response in new_responses:
        resp = response.get('responses', {})

        # Prior MH treatment
        if resp.get('BPG_MH') == '2':
            baseline['risk_factors']['prior_mh'] += 1

        # MH medications
        if resp.get('PRE_RX') == '2' and resp.get('PRE_RX_MH') in ['Yes', 'Not sure']:
            baseline['risk_factors']['mh_meds'] += 1

        # Poor health
        if resp.get('HTH_GEN') in ['4', '5']:
            baseline['risk_factors']['poor_health'] += 1

        # No exercise
        if resp.get('PRE_EXER') == '1':
            baseline['risk_factors']['no_exercise'] += 1

        # Dieting
        if resp.get('PRE_DIET') == '2':
            baseline['risk_factors']['dieting'] += 1

        # Overweight/obese
        if resp.get('OWGT_OBS') == '2':
            baseline['risk_factors']['overweight'] += 1

    # Merge care settings (only non-missing)
    for response in new_responses:
        routing = response.get('routing', {})
        setting = routing.get('setting_name')
        if setting and setting != 'Unknown':
            baseline['care_settings'][setting] = \
                baseline['care_settings'].get(setting, 0) + 1

    return baseline
