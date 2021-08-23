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
root_path = os.path.abspath(os.path.join(os.getcwd(), "./"))
eqls_df = pd.read_csv(root_path + "/data-analysis/data/UKDA-7724-csv/csv/eqls_2011.csv")

# Creating categorical variable
eqls_df["Y11_Country_cat"] = eqls_df["Y11_Country"].apply(lambda x: categorical_data_config.YY11_Country.get(x))
eqls_df["Y11_HH2a_cat"] = eqls_df["Y11_HH2a"].apply(lambda x: categorical_data_config.Y11_HH2a.get(x))


numerical = [
    'Y11_Country', 'Y11_Q31', 'Y11_ISCEDsimple', 'Y11_Q49', 'Y11_Agecategory', 'Y11_HH2a',
    'Y11_HHsize'
]
pal = dict(Male="seagreen", Female=".7")

def annotate(data, **kws):
    n = len(data)
    ax = plt.gca()
    ax.text(.1, .9, f"N = {n}", transform=ax.transAxes)


cond_facet_grid = sns.FacetGrid(data=eqls_df, col='Y11_Country_cat', palette=pal, sharey=True, sharex=True, hue='Y11_HH2a_cat', col_wrap=4,
                                margin_titles=True)
cond_facet_grid.map_dataframe(sns.scatterplot, x='Y11_Q42', y='Y11_SocExIndex')
cond_facet_grid.map_dataframe(annotate)
cond_facet_grid.fig.subplots_adjust(wspace=.1, hspace=.05)

for ax in cond_facet_grid.axes.flat:
    print(ax.get_xlabel())
    ax.set_xlabel(ax.get_xlabel(), fontsize='x-large')
    ax.set_ylabel(ax.get_ylabel(), fontsize='x-large')
    ax.tick_params(labelleft=True)

plt.subplots_adjust(wspace=0.1, hspace=0.4)
plt.legend(bbox_to_anchor=(1.10, 0.8), loc=2)
plt.show()