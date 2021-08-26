# Codebase walkthrough for `rds-course`
## :memo: Documentation
This README details the code within the jupyter notebooks that support the Research Data Science Course. The code is separated 
into 4 notebooks:
### :minidisc: [Handling_data](data-analysis/Handling_data.ipynb) 
- a notebook containing code to load in the data and clean the feature 
  columns to ensure there are more intuitive names given to features.
### :pencil2: [Data_description](data-analysis/Data_description.ipynb) 
- a notebook containing code to clean data and employ several strategies to deal with missing data
- identifying columns which contain missing data and dropping the features 
- dropping features with a high proportion of missing data (>50%) and imputing the others with less missing data
- Imputation strategy uses the `mean` of any nominal and scalar variable and the `mode` of any classified `object` and `string` features 
### :amphora: [Modelling_data](data-analysis/Modelling_data.ipynb) 
- a notebook containing code to build a `LogisticRegression` model
to classify `"poor health"` and `"good health"`. Basic model scoring and evaluation using confusion matrix.
### :speech_balloon: [Model_evaluation](data-analysis/Model_evaluation.ipynb) 
- a notebook containing model evaluation 
  - confusion matrices to analyse precision, accuracy and recall 
  - coefficient analysis for each of the features
  - feature importance graphs showing the most influential features on model predictions
  - Model performance on country-specific testing data (UK, Netherlands and Romania)

## :bookmark: Scripts
There are several scripts within the [scripts_directory](data-analysis/scripts) to visualise the data for data exploration and 
provide helper functions to parse the data. 
### :monocle_face: Parsing data
- [`categorical_variable_mapping`](data-analysis/scripts/categorical_variable_mapping.py) - this allows us to map the numerical classifications
to textual classifications to identify each features for data description.
- [`eqls_box_plot`](data-analysis/scripts/eqls_box_plot.py) - this script produces a boxplot that showing the distribution of some of the key 
variables associated with the "self-reported health" outcome.
- [`eqls_count_plot`](data-analysis/scripts/eqls_count_plot.py) - this script produces a countplot to total the number and distribution 
of responses across key variables in the survey.
- [`eqls_missing_data_plot`](data-analysis/scripts/eqls_missing_data_plot.py) - this script allows us to produce a data "missingness" plot for key features 
used in the model.
- [`eqls_ridgeline_plot`](data-analysis/scripts/eqls_ridgeline_plot.py) - this script produced ridgeline plots showcasing the distribution of responses for 
each country in their "self-reported health".
- [`eqls_condition_plot`](data-analysis/scripts/eqls_condition_plot.py) - this is a conditionplot to establish the relationship between key features and 
the measure of "self-reported health" used.

## :sparkles: Key features
The highest `Wave 3` missingness is coming from the following subset of questions:
```
Difficult_to_use_child_care_because_of_cost                                                  83%
Difficult_to_use_child_care_because_of_availability                                          83%
Difficult_to_use_child_care_because_of_access                                                83%
Difficult_to_use_child_care_because_of_quality_of_care                                       83%
Difficult_to_use_long_term_care_because_of_cost                                              90%
Difficult_to_use_long_term_care_because_of_availability                                      89%
Difficult_to_use_long_term_care_because_of_access                                            89%
Difficult_to_use_long_term_care_because_of_quality_of_care                                   90%
```
The available features contain data about childcare availability. The literature indicates that one member of each 
household was surveyed, could indicate a large amount of non-family households, and members of households who may not 
deal with childcare are the interviewee.