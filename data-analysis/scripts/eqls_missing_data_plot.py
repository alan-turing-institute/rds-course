# Program to visualize missing values in dataset

# Importing the libraries
import os
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# load array
root_path = os.path.abspath(os.path.join(os.getcwd(), "./"))

feature_2011_other_countries_columns = pd.read_csv(str(root_path)+"/data-analysis/data/derived_data/eqls_2011_modelled.csv")

eqls_features_df = feature_2011_other_countries_columns[['How_often_felt_cheerful_and_in_good_spirits_last_2_weeks',
                                                         'How_frequently_take_part_in_sports_or_exercise',
                                                         'Degree_of_urbanisation',
                                                         'Access_to_banking_services',
                                                         'Financial_situation_of_your_household_compared_to_12_months_ago',
                                                         'A_person_to_get_support_from_to_raise_emergency_money',
                                                         'How_happy_are_you',
                                                         'Come_home_from_work_too_tired_to_do_some_of_the_household_jobs',
                                                         'Education_completed',
                                                         'How_much_tension_between_Old_and_Young_people',
                                                         'Age',
                                                         'How_often_felt_active_and_vigorous_last_2_weeks',
                                                         'Difficult_to_see_a_doctor_because_of_distance',
                                                         'How_often_woke_up_feeling_fresh_and_rested_last_2_weeks',
                                                         'How_often_felt_your_daily_life_has_been_filled_with_things_that_interest_you_last_2_weeks',
                                                         'How_satisfied_with_social_life',
                                                         'Country_group',
                                                         'The_share_of_housework_you_do_is_',
                                                         'How_often_felt_downhearted_and_depressed_last_2_weeks',
                                                         'Employment__7_groups',
                                                         'Income_quartiles',
                                                         'As_much_time_as_would_like_on_own_hobbiesinterests',
                                                         'How_often_felt_calm_and_relaxed_last_2_weeks',
                                                         'People_look_down_on_me_because_of_my_job_situation_or_income',
                                                         'DV_Anyone_usedwould_have_like_to_use_long_term_care_last_12_months',
                                                         'I_generally_feel_that_what_I_do_in_life_is_worthwhile'
                                                         ]]

# Visualize the correlation between the number of
# missing values in different columns as a heatmap
plt.figure(figsize=(80, 40))
sns.displot(
    data=eqls_features_df.isna().melt(value_name="missing"),
    y="variable",
    hue="missing",
    multiple="fill",
    aspect=1.25
)
plt.savefig(str(root_path)+"/data-analysis/plots/eqls_missingness_plot.png")
plt.show()
