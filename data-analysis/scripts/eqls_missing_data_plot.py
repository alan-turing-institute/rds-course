# Program to visualize missing values in dataset

# Importing the libraries
from pathlib import Path
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# load array
root_data_path = Path("data")

feature_2011_other_countries_columns = pd.read_csv(str(root_data_path)+f"/derived_data/eqls_2011_modelled.csv")

eqls_features_df = feature_2011_other_countries_columns[['Country',
                                                         'DV_Any_limitingnot_limiting_chronic_health_problem',
                                                         'How_satisfied_with_health',
                                                         'Limited_by_chronic_health_problems',
                                                         'Chronic_health_problems',
                                                         'How_often_felt_active_and_vigorous_last_2_weeks',
                                                         'Difficult_to_see_a_doctor_because_of_distance',
                                                         'EQLS_Wave',
                                                         'Age',
                                                         'How_often_felt_cheerful_and_in_good_spirits_last_2_weeks',
                                                         'How_frequently_take_part_in_sports_or_exercise',
                                                         'Limited_by_chronic_health_problems',
                                                         'Degree_of_urbanisation',
                                                         'Access_to_banking_services',
                                                         'Financial_situation_of_your_household_compared_to_12_months_ago',
                                                         'A_person_to_get_support_from_to_raise_emergency_money',
                                                         'How_happy_are_you',
                                                         'Come_home_from_work_too_tired_to_do_some_of_the_household_jobs',
                                                         'Education_completed',
                                                         'How_much_tension_between_Old_and_Young_people'
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
plt.show()