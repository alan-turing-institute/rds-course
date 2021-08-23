
# import bootstrap  # noqa
import os
import plotly.express as px
# plotting
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
from categorical_variable_mapping import CategoricalDataConfig

categorical_data_config = CategoricalDataConfig()

# settings
plt.style.use('seaborn')
sns.set_theme(style="whitegrid")
sns.set_style("white")
plt.rcParams["figure.figsize"] = (16, 8)

# Loading the dataset
root_path = os.path.abspath(os.path.join(os.getcwd(), "../"))
eqls_df = pd.read_csv(root_path+"/data/UKDA-7724-csv/csv/eqls_2011.csv")

eqls_df["Y11_Country_cat"] = eqls_df["Y11_Country"].apply(lambda x: categorical_data_config.YY11_Country.get(x))
eqls_df["Y11_Q31_cat"] = eqls_df["Y11_Q31"].apply(lambda x: categorical_data_config.Y11_Q31.get(x))
eqls_df["Y11_ISCEDsimple_cat"] = eqls_df["Y11_ISCEDsimple"].apply(lambda x: categorical_data_config.Y11_ISCEDsimple.get(x))
eqls_df["Y11_Q49_cat"] = eqls_df["Y11_Q49"].apply(lambda x: categorical_data_config.Y11_Q49.get(x))
eqls_df["Y11_Agecategory_cat"] = eqls_df["Y11_Agecategory"].apply(lambda x: categorical_data_config.Y11_Agecategory.get(x))
eqls_df["Y11_HH2a_cat"] = eqls_df["Y11_HH2a"].apply(lambda x: categorical_data_config.Y11_HH2a.get(x))
eqls_df["Y11_HHsize_cat"] = eqls_df["Y11_HHsize"].apply(lambda x: categorical_data_config.Y11_HHsize.get(x))


categorical = [
  'Y11_Country_cat', 'Y11_Q31_cat', 'Y11_ISCEDsimple_cat', 'Y11_Q49_cat', 'Y11_Agecategory_cat', 'Y11_HH2a_cat', 'Y11_HHsize_cat'
]

fig, ax = plt.subplots(2, 3, figsize=(20, 10))

for variable, subplot in zip(categorical, ax.flatten()):
    sns.countplot(eqls_df[variable], ax=subplot)
    for label in subplot.get_xticklabels():
        label.set_rotation(90)
# import bootstrap  # noqa
import os
import plotly.express as px
# plotting
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
from categorical_variable_mapping import CategoricalDataConfig

categorical_data_config = CategoricalDataConfig()
# settings
plt.style.use('seaborn')
sns.set_theme(style="whitegrid")
sns.set_style("white")
plt.rcParams["figure.figsize"] = (16, 8)
plt.clf()
plt.cla()
plt.close()


# Loading the dataset
root_path = os.path.abspath(os.path.join(os.getcwd(), "../"))
eqls_df = pd.read_csv(root_path + "/data/UKDA-7724-csv/csv/eqls_2011.csv")

# Creating categorical variable
eqls_df["Y11_Country_cat"] = eqls_df["Y11_Country"].apply(lambda x: categorical_data_config.YY11_Country.get(x))


numerical = [
    'Y11_Country_cat', 'Y11_Q31', 'Y11_ISCEDsimple', 'Y11_Q49', 'Y11_Agecategory', 'Y11_HH2a',
    'Y11_HHsize'
]

fig, ax = plt.subplots(2, 3, figsize=(20, 10))
fig.subplots_adjust(hspace=.5)

for variable, subplot in zip(numerical, ax.flatten()):
    if variable == "Y11_Country_cat":
        sorted_nb = eqls_df.groupby([variable])['Y11_Q42'].median().sort_values()
        sns.boxplot(x=eqls_df[variable], y=eqls_df['Y11_Q42'], ax=subplot, order=list(sorted_nb.index))
    else:
        sns.boxplot(x=eqls_df[variable], y=eqls_df['Y11_Q42'], ax=subplot)
    for label in subplot.get_xticklabels():
        label.set_rotation(90)

plt.xlabel("Self-reported health")
plt.ylabel("Count")
# add title
plt.title('Boxplot of european self-reported health in 2011')
plt.legend(bbox_to_anchor=(.80, 0.8), loc=2);
plt.show()