from typing import Dict

import numpy as np
import pandas as pd


# note only tested on "Y11_Country" var
def parse_categorical_values(
    categorical_values_df: pd.DataFrame,
    var_name_col: str,
    var_name: str,
    values_col: str,
) -> Dict[str, str]:
    rows = categorical_values_df[categorical_values_df[var_name_col] == var_name]
    if len(rows) > 1:
        raise ValueError(
            f"something has gone wrong, more than one row matches var name: {var_name}"
        )
    row = rows.iloc[0]
    vals_string = row[values_col]
    # lines look like: "encoded_val = human_readable_val" so split on " = "
    mapping = dict([line.split(" = ") for line in vals_string.split("\n")])
    # ensure keys are ints
    mapping = {int(k): v for k, v in mapping.items()}
    return mapping


def parse_country_values_2011(categorical_values_df: pd.DataFrame) -> Dict[str, str]:
    return parse_categorical_values(
        categorical_values_df=categorical_values_df,
        var_name_col="Variable name",
        var_name="Y11_Country",
        values_col="Values if present - 2011",
    )


def check_dataset_load(df):
    """Check data frame loaded correctly for 'Load and Explore' exercise"""
    try:
        assert isinstance(df, pd.DataFrame), "❌ df is not a DataFrame" # check we've loaded data into a DataFrame
        assert len(df) == 79270, "❌ unexpected no. of rows" # check number of rows matches expected
        print("✅ df loaded correctly")
    except AssertionError as e:
        print(e)


def check_dataset_explored(n_columns, n_float64_columns, Y11_Q31_mean_value, Y11_Country_n_unique):
    # not using assert statements as they give away the answers!
    correct = 0

    n_columns_result = "✅ correct" if n_columns == 199 else "❌ incorrect"
    n_float64_result = "✅ correct" if n_float64_columns == 187 else "❌ incorrect"
    Y11_Q31_mean_value_result = "✅ correct" if np.isclose(Y11_Q31_mean_value, 1.856049) else "❌ incorrect"
    Y11_Country_n_unique_result = "✅ correct" if Y11_Country_n_unique == 35 else "❌ incorrect"

    print(f"n_columns answer {n_columns_result}")
    print(f"n_float64_columns answer {n_float64_result}")
    print(f"Y11_Q31_mean_value answer {Y11_Q31_mean_value_result}")
    print(f"Y11_Country_n_unique answer {Y11_Country_n_unique_result}")

    
# manually pasted the answer here but not the code
desired_column_mapping = {
    "Wave": "eqls_wave",
    "Y11_Country": "country",
    "Y11_Q31": "marital_status",
    "Y11_Q32": "no_of_children",
    "Y11_ISCEDsimple": "education_completed",
    "Y11_Q49": "rural_urban_living",
    "Y11_Q67_1": "citizenship_country",
    "Y11_Q67_2": "citizenship_another_eu_member",
    "Y11_Q67_3": "citizenship_a_non_eu_country",
    "Y11_Q67_4": "citizenship_dont_know",
    "Y11_Q67_5": "citizenship_refusal",
    "Y11_Agecategory": "age",
    "Y11_HH2a": "gender",
    "Y11_HHsize": "household_size",
    "Y11_HHsize18plus": "household_size_over_18",
    "Y11_HHstructure": "household_structure",
    "Y11_Education": "education_3_groups",
    "Y11_EmploymentStatus": "employment_7_groups",
    "Y11_Incomequartiles_percapita": "income_quartiles",
    "Y11_RuralUrban": "dv_rural_urban_living",
    "Y11_Degurba": "degree_of_urbanisation",
    "Y11_CountryGroupEU28": "country_group",
    "Y11_Q33a": "direct_contact_with_children",
    "Y11_Q33b": "direct_contact_with_parents",
    "Y11_Q33c": "direct_contact_with_other_relatives",
    "Y11_Q33d": "direct_contact_with_neighbours",
    "Y11_Q34a": "phone_internet_contact_with_children",
    "Y11_Q34b": "phone_internet_contact_with_parents",
    "Y11_Q34c": "phone_internet_contact_with_other_relatives",
    "Y11_Q34d": "phone_internet_contact_with_neighbours",
    "Y11_Q35a": "a_person_to_get_support_from_to_help_around_house_",
    "Y11_Q35b": "a_person_to_get_advice_from_about_a_personal_family_matter",
    "Y11_Q35c": "a_person_to_get_support_from_when_looking_for_a_job",
    "Y11_Q35d": "a_person_to_get_support_from_when_feeling_depressed",
    "Y11_Q35e": "a_person_to_get_support_from_to_raise_emergency_money",
    "Y11_Q42": "health_condition",
    "Y11_Q43": "chronic_health_problems_",
    "Y11_Q44": "limited_by_chronic_health_problems_",
    "Y11_Q17": "no_of_rooms_in_accommodation",
    "Y11_Q18": "tenure",
    "Y11_Q19a": "problems_with_accommodation_space",
    "Y11_Q19b": "problems_with_accommodation_rot_in_windows_etc_",
    "Y11_Q19c": "problems_with_accommodation_damp_or_leaks",
    "Y11_Q19d": "problems_with_accommodation_no_toilet",
    "Y11_Q19e": "problems_with_accommodation_no_bath_shower",
    "Y11_Q19f": "problems_with_accommodation_no_outside_space",
    "Y11_Q20": "likelihood_of_leaving_accom_within_6_months",
    "Y11_Q50a": "neighbourhood_problems_noise",
    "Y11_Q50b": "neighbourhood_problems_air_quality",
    "Y11_Q50c": "neighbourhood_problems_quality_of_drinking_water",
    "Y11_Q50d": "neighbourhood_problems_crime_violence_or_vandalism",
    "Y11_Q50e": "neighbourhood_problems_litter_or_rubbish",
    "Y11_Q50f": "neighbourhood_problems_traffic",
    "Y11_Accommproblems": "no_of_problems_with_accommodation",
    "Y11_Q47a": "difficult_to_see_a_doctor_because_of_distance_",
    "Y11_Q47b": "difficult_to_see_a_doctor_because_of_delay_in_getting_appointment_",
    "Y11_Q47c": "difficult_to_see_a_doctor_because_of_waiting_time_",
    "Y11_Q47d": "difficult_to_see_a_doctor_because_of_cost_",
    "Y11_Q47e": "difficult_to_see_a_doctor_because_of_lack_of_time_",
    "Y11_Q51a": "access_to_postal_services_",
    "Y11_Q51b": "access_to_banking_services_",
    "Y11_Q51c": "access_to_public_transport_",
    "Y11_Q51d": "access_to_cinema_theatre_and_cultural_centre_",
    "Y11_Q51e": "access_to_recreational_or_green_areas_",
    "Y11_Q52": "how_much_time_spent_on_travelling_to_work_study_",
    "Y11_Q53a": "quality_of_health_services_",
    "Y11_Q53b": "quality_of_education_system_",
    "Y11_Q53c": "quality_of_public_transport_",
    "Y11_Q53d": "quality_of_child_care_services_",
    "Y11_Q53e": "quality_of_long_term_care_services_",
    "Y11_Q53f": "quality_of_social_municipal_housing_",
    "Y11_Q53g": "quality_of_state_pension_system_",
    "Y11_Q54a_1": "i_or_someone_else_in_household_used_child_care_in_12_months",
    "Y11_Q54a_2": "someone_close_outside_household_used_child_care_in_12_months",
    "Y11_Q54a_3": "nobody_used_child_care_in_12_months",
    "Y11_Q54a_4": "child_care_used_in_12_months_dont_know",
    "Y11_Q54a_5": "child_care_used_in_12_months_refusal",
    "Y11_Q54b_1": "i_or_someone_else_in_household_used_long_term_care_in_12_months",
    "Y11_Q54b_2": "someone_close_outside_household_used_long_term_care_in_12_months",
    "Y11_Q54b_3": "nobody_used_long_term_care_in_12_months",
    "Y11_Q54b_4": "long_term_care_used_in_12_months_dont_know",
    "Y11_Q54b_5": "long_term_care_used_in_12_months_refusal",
    "Y11_Q55a": "difficult_to_use_child_care_because_of_cost_",
    "Y11_Q55b": "difficult_to_use_child_care_because_of_availability_",
    "Y11_Q55c": "difficult_to_use_child_care_because_of_access_",
    "Y11_Q55d": "difficult_to_use_child_care_because_of_quality_of_care_",
    "Y11_Q56a": "difficult_to_use_long_term_care_because_of_cost_",
    "Y11_Q56b": "difficult_to_use_long_term_care_because_of_availability_",
    "Y11_Q56c": "difficult_to_use_long_term_care_because_of_access_",
    "Y11_Q56d": "difficult_to_use_long_term_care_because_of_quality_of_care_",
    "Y11_Q24": "can_most_people_be_trusted_",
    "Y11_Q25a": "how_much_tension_between_poor_and_rich_",
    "Y11_Q25b": "how_much_tension_between_management_and_workers_",
    "Y11_Q25c": "how_much_tension_between_men_and_women_",
    "Y11_Q25d": "how_much_tension_between_old_and_young_people_",
    "Y11_Q25e": "how_much_tension_between_different_racial_ethnic_groups_",
    "Y11_Q25f": "how_much_tension_between_different_religious_groups_",
    "Y11_Q25g": "how_much_tension_between_groups_with_different_sexual_orientation_",
    "Y11_Q28a": "how_much_trust_the_parliament_",
    "Y11_Q28b": "how_much_trust_the_legal_system_",
    "Y11_Q28c": "how_much_trust_the_press_",
    "Y11_Q28d": "how_much_trust_the_police_",
    "Y11_Q28e": "how_much_trust_the_government_",
    "Y11_Q28f": "how_much_trust_the_local_authorities_",
    "Y11_Q21a": "how_frequently_attend_religious_services_",
    "Y11_Q21b": "how_frequently_use_the_internet_other_than_for_work_",
    "Y11_Q21c": "how_frequently_take_part_in_sports_or_exercise_",
    "Y11_Q21d": "how_frequently_participate_in_social_activities_",
    "Y11_Q22a": "how_often_worked_unpaid_for_community_services_last_12_months_",
    "Y11_Q22b": "how_often_worked_unpaid_for_education_cultural_etc_organisation_last_12_months_",
    "Y11_Q22c": "how_often_worked_unpaid_for_social_movements_charities_last_12_months_",
    "Y11_Q22d": "how_often_worked_unpaid_for_political_parties_or_trade_unions_last_12_months_",
    "Y11_Q22e": "how_often_worked_unpaid_for_other_voluntary_org_last_12_months_",
    "Y11_Q23a": "attended_a_trade_union_political_party_meeting_last_12_months_",
    "Y11_Q23b": "attended_a_protest_or_demonstration_last_12_months_",
    "Y11_Q23c": "signed_a_petition_last_12_months_",
    "Y11_Q23d": "contacted_a_politician_last_12_months_",
    "Y11_Q29e": "feel_left_out_of_sociey_",
    "Y11_Q29f": "cant_find_the_way_because_life_has_become_so_complicated_",
    "Y11_Q29g": "the_value_of_what_i_do_is_not_recognised_by_others_",
    "Y11_Q29h": "people_look_down_on_me_because_of_my_job_situation_or_income_",
    "Y11_Q29i": "feel_close_to_people_in_the_area_where_i_live",
    "Y11_SocExIndex": "social_exclusion_index",
    "Y11_Volunteering": "volunteering_frequency",
    "Y11_Q57": "personal_financial_situation",
    "Y11_Q58": "household_able_to_make_ends_meet_",
    "Y11_Q59a": "can_afford_to_keep_home_adequately_warm_",
    "Y11_Q59b": "can_afford_to_pay_for_a_weeks_annual_holiday_away_",
    "Y11_Q59c": "can_afford_to_replace_any_worn_out_furniture_",
    "Y11_Q59d": "can_afford_a_meal_with_meat_chicken_fish_every_second_day_",
    "Y11_Q59e": "can_afford_to_buy_new_rather_than_second_hand_clothes_",
    "Y11_Q59f": "can_afford_to_have_friends_or_family_for_a_drink_meal_at_least_once_a_month_",
    "Y11_Q60a": "rent_mortgage_payments_for_accommodation",
    "Y11_Q60b": "utility_bills_such_as_electricity_water_gas",
    "Y11_Q60c": "payments_for_consumer_loans_credit_cards",
    "Y11_Q60d": "payments_for_informal_loans_from_friends_relatives",
    "Y11_Q65": "financial_situation_of_your_household_compared_to_12_months_ago_",
    "Y11_Q66": "household_financial_expectations_for_th_12_months_",
    "Y11_Deprindex": "deprivation_index_no_of_items_hhold_cant_afford",
    "Y11_Q29a": "i_am_optimistic_about_the_future",
    "Y11_Q29b": "i_generally_feel_that_what_i_do_in_life_is_worthwhile",
    "Y11_Q29c": "i_feel_i_am_free_to_decide_how_to_live_my_life",
    "Y11_Q29d": "i_seldom_have_time_to_do_the_things_i_really_enjoy",
    "Y11_Q30": "how_satisfied_with_life_these_days_",
    "Y11_Q40a": "how_satisfied_with_education_",
    "Y11_Q40b": "how_satisfied_with_present_job_",
    "Y11_Q40c": "how_satisfied_with_present_standard_of_living_",
    "Y11_Q40d": "how_satisfied_with_accommodation_",
    "Y11_Q40e": "how_satisfied_with_family_life_",
    "Y11_Q40f": "how_satisfied_with_health_",
    "Y11_Q40g": "how_satisfied_with_social_life_",
    "Y11_Q40h": "how_satisfied_with_economic_situation_in_the_country_",
    "Y11_Q41": "how_happy_are_you_",
    "Y11_Q45a": "how_often_felt_cheerful_and_in_good_spirits_last_2_weeks_",
    "Y11_Q45b": "how_often_felt_calm_and_relaxed_last_2_weeks_",
    "Y11_Q45c": "how_often_felt_active_and_vigorous_last_2_weeks_",
    "Y11_Q45d": "how_often_woke_up_feeling_fresh_and_rested_last_2_weeks_",
    "Y11_Q45e": "how_often_felt_your_daily_life_has_been_filled_with_things_that_interest_you_last_2_weeks_",
    "Y11_Q46a": "how_often_felt_particularly_tense_last_2_weeks_",
    "Y11_Q46b": "how_often_felt_lonely_last_2_weeks_",
    "Y11_Q46c": "how_often_felt_downhearted_and_depressed_last_2_weeks_",
    "Y11_MWIndex": "who_5_mental_wellbeing_index",
    "w4": "final_weight_trimmed_and_standardised",
    "w5_EU28": "cross_national_weight_eu28_to_calculate_averages_for_all_eu_in_2013_incl_croatia_",
    "w5_total": "weight_5_total",
    "Y11_Q7": "how_many_hours_work_per_week_in_1st_job_",
    "Y11_Q8": "how_many_hours_per_week_would_you_prefer_to_work_at_present_",
    "Y11_Q9": "how_many_hours_does_your_partner_work_per_week_",
    "Y11_Q10": "how_many_hours_per_week_would_you_prefer_your_partner_to_work_",
    "Y11_Q11": "working_hours_fit_with_family_social_commitments_",
    "Y11_Q12a": "come_home_from_work_too_tired_to_do_some_of_the_household_jobs",
    "Y11_Q12b": "difficult_to_fulfil_family_responsibilities_because_of_the_time_at_work",
    "Y11_Q12c": "difficult_to_concentrate_at_work_because_of_family_responsibilities",
    "Y11_Q15": "how_likely_to_lose_job_in_6_months_",
    "Y11_Q16": "how_likely_to_find_another_job_of_similar_salary_",
    "Y11_Q36a": "how_often_care_for_your_children_",
    "Y11_Q36b": "how_often_cook_and_doing_housework_",
    "Y11_Q36c": "how_often_care_for_elderly_or_disabled_relatives_",
    "Y11_Q38": "the_share_of_housework_you_do_is_",
    "Y11_Q39a": "as_much_time_as_would_like_with_family_members_",
    "Y11_Q39b": "as_much_time_as_would_like_with_others_not_family_",
    "Y11_Q39c": "as_much_time_as_would_like_on_own_hobbies_interests_",
    "Y11_Q39d": "as_much_time_as_would_like_on_voluntary_work_",
    "Y11_Strainbasedconflict": "work_life_balance_conflict_",
    "Y11_Q7a": "worked_at_an_additional_paid_job_last_4_weeks_",
    "Y11_Q7b": "how_many_hours_per_week_worked_in_the_additional_job_",
    "DV_Q7": "dv_total_number_of_working_hours",
    "DV_Q67": "dv_citizenship",
    "DV_Q43Q44": "dv_any_limiting_not_limiting_chronic_health_problem_",
    "DV_Q54a": "dv_anyone_used_would_have_like_to_use_child_care_last_12_months_",
    "DV_Q54b": "dv_anyone_used_would_have_like_to_use_long_term_care_last_12_months_",
    "DV_Q55": "dv_no_of_factors_which_made_it_difficult_to_use_child_care_",
    "DV_Q56": "dv_no_of_factors_which_made_it_difficult_to_use_long_term_care_",
    "DV_Q8": "dv_preferred_working_hours_3_groups_",
    "DV_Q10": "dv_preferred_working_hours_of_respondents_partner_3_groups_",
    "ISO3166_Country": "iso3166_country_url",
    "RowID": "rowid_for_the_uk_data_service_public_api",
    "URIRowID": "root_uri_for_a_row_respondent_that_displays_all_data_values_for_a_single_row_via_the_uk_data_service_public_api",
    "UniqueID": "unique_respondent_id",
}    

    
def check_column_mapping(column_mapping, df):
    """Check column mapping for 'Making Things More Readable' exercise"""
    # check each in turn to give best error
    print("Checking each column...")
    for old_val in desired_column_mapping.keys():
        try:
            assert (
                column_mapping[old_val] == desired_column_mapping[old_val]
            ), f"""❌ mismatch at {old_val}.
    Got: {column_mapping[old_val]}, expected: {desired_column_mapping[old_val]}"
    Exiting check. There may be further errors."""
        except KeyError as e:
            print(
                "❌ Encountered a KeyError. This means the expected key isn't in your column mapping!"
            )
            raise e

    print("✅ Column mapping correct... Checking df columns set correctly...")
    assert all(
        df.columns == list(desired_column_mapping.values())
    ), "❌ New column names not set on df"

    # otherwise...
    print("✅ Success!")


def set_column_mapping(df, eqls_api_map_df):
    """Set column mapping for 'Making Things More Readable' exercise"""
    old_cols = eqls_api_map_df["VariableName"]

    # The 4 .str calls below:
    #  convert to lowercase
    #  remove apostrophes
    #  replace whitespace with _
    #  rremove consecutive underscores
    new_cols = eqls_api_map_df["VariableLabel"].str.lower()\
                                            .str.replace("'",'')\
                                            .str.replace('[^\w]','_')\
                                            .str.replace("_+", "_")

    column_mapping = dict(zip(old_cols, new_cols))

    # Apply your column mapping to df
    df = df.rename(columns=column_mapping)
    return df
