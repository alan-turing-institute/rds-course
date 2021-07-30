import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.patches as mpatches
# read the data from here https://ourworldindata.org/us-states-vaccinations
df_vaccination = pd.read_csv('../data/us-covid-share-fully-vaccinated.csv', sep=',', parse_dates=['Day'])

# look at max day avalaible for cumulative vaccination data
max_day = df_vaccination['Day'].max()
df_vaccination_max = df_vaccination[df_vaccination['Day']==max_day]

# get election data from here https://dataverse.harvard.edu/file.xhtml?fileId=4299753&version=6.0
df_president_2020 = pd.read_csv('../data/2020-president.csv', sep=',')

df_president_2020 = df_president_2020[df_president_2020['year']==2020]

# making sure state names are compatible between datasets
df_president_2020['state'] = df_president_2020['state'].str.title()
# calculate percentage of votes for a party
df_president_2020['party_percentage'] = df_president_2020['candidatevotes']/df_president_2020['totalvotes']

# only select data from the winner party
index_list = []
for state in np.unique(df_president_2020['state']):
   max = df_president_2020[df_president_2020['state']==state]['party_percentage'].max()
   index =  (df_president_2020[(df_president_2020['state'] == state) & (df_president_2020['party_percentage']==max)].index.values[0])
   index_list.append(index)
df_president_2020_party = df_president_2020.loc[index_list]

# join the datasets
df_joined = pd.merge(df_vaccination_max,df_president_2020_party[['state','party_simplified','party_percentage']],left_on='Entity',right_on='state',how='inner')

# make percentage as a share of democrat vote (this is not 100% right, we don't consider other parties, however they are negligible).
df_joined.loc[df_joined[df_joined['party_simplified']=='REPUBLICAN'].index,'party_percentage'] = 1- df_joined[df_joined['party_simplified']=='REPUBLICAN']['party_percentage']
df_joined.sort_values(by='people_fully_vaccinated_per_hundred',inplace=True, ascending=False)


## PLOTS

# Use color a category
import matplotlib.pyplot as plt
sns.set_theme(style="whitegrid")
sns.set_style("white")

f, ax = plt.subplots(figsize=(10, 15))
# Load the dataset
ax = sns.barplot(x="people_fully_vaccinated_per_hundred", y="state", data=df_joined,hue='party_simplified',dodge=False)
ax.set_title('US: Share of the population fully vaccinated against COVID-19 and 2020 presidential election vote',fontsize=12)
ax.set_xlabel(' Share of the population fully vaccinated against COVID-19 (%)')
ax.legend_.set_title("2020 election winner party")
sns.despine(left=False, bottom=False)
plt.show()

# Use color a scale
f2, ax2 = plt.subplots(figsize=(10, 15))
cmap = sns.color_palette("vlag_r", n_colors=51)
# Load the example car crash dataset
ax2 = sns.barplot(x="people_fully_vaccinated_per_hundred", y="state", data=df_joined,hue='party_percentage',dodge=False,palette=cmap)
ax2.set_title('US: Share of the population fully vaccinated against COVID-19 and party share vote on the 2020 presidential election vote',fontsize=12)
ax2.set_xlabel('Share of the population fully vaccinated against COVID-19 (%)')
sns.despine(left=False, bottom=False)
# Add a legend and informative axis label
sns.despine(left=False, bottom=False)
# Create a new legend
party_min = mpatches.Patch(color=cmap[0], label='{:.2f}'.format(df_joined['party_percentage'].min()))
party_max = mpatches.Patch(color=cmap[-1], label='{:.2f}'.format(df_joined['party_percentage'].max()))
ax2.legend(handles=[party_max,party_min],title='Share of Democrat vote (%)')
plt.show()


