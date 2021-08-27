import os
# plotting
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
# from categorical_variable_mapping import CategoricalDataConfig

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

def label(x, color, label):
    ax = plt.gca()
    ax.text(-0.1, .2, label, fontweight="bold", color="black",
            ha="left", va="center", transform=ax.transAxes)

ridge_plot = sns.FacetGrid(eqls_df, row="Y11_Country_cat", hue="Y11_Country_cat", aspect=5, height=1.25)

# Draw the densities in a few steps
ridge_plot.map(sns.kdeplot, "Y11_Q42", clip_on=False, shade=True, alpha=0.7, lw=4, bw=.2)
ridge_plot.map(plt.axhline, y=0, lw=4, clip_on=False)
ridge_plot.map(label, "Y11_Country_cat")
locs, labels = plt.xticks()

plt.xlabel('Self-reported health')
# Set the subplots to overlap
ridge_plot.fig.subplots_adjust(hspace=-0.01)
# Remove axes details that don't play well with overlap
ridge_plot.set_titles("")
ridge_plot.set(yticks=[])
ridge_plot.despine(bottom=True, left=True)
plt.xticks(locs[1:6], list(categorical_data_config.Y11_Q42.values()))

plt.show()
plt.savefig(str(root_path)+"/data-analysis/plots/eqls_ridgeline_plot.png")