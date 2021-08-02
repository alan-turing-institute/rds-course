# general
import pandas as pd
import numpy as np
from datetime import datetime
import plotly.express as px
# plotting
import seaborn as sns
import matplotlib.pyplot as plt
# settings

plt.style.use('seaborn')
sns.set_theme(style="whitegrid")
sns.set_style("white")
plt.rcParams["figure.figsize"] = (16, 8)
df_uk_cases = pd.read_csv('../data/data_2021-Aug-01.csv', sep=',', parse_dates=['date'])
df_uk_cases_1y = df_uk_cases[(df_uk_cases['date']>='2020-06-06') & (df_uk_cases['date']<'2021-06-01')]


def normalise(cases,country):
    # population estimates from https://www.ons.gov.uk/peoplepopulationandcommunity/populationandmigration/populationestimates/datasets/populationestimatesforukenglandandwalesscotlandandnorthernireland
    norm =  {'England': 56550138, 'Wales': 3169586, 'Scotland': 5466000, 'Northern Ireland': 1895510}
    return cases / norm[country] *100000

df_uk_cases_1y['casesNormalised'] = df_uk_cases_1y.apply(lambda row: normalise(row.newCasesBySpecimenDate, row.areaName),axis=1)

df_uk_cases_1y['cases'] = df_uk_cases_1y['casesNormalised'].rolling(window=7).mean()

sns.lineplot(data=df_uk_cases_1y,x='date',y='cases',hue='areaName',legend='full')
# add title
plt.title('Covid-19 case rate per 100.000 people between 6th of June 2020 and 1st of June 2021')
# move the legend outside of the main figure
plt.legend(bbox_to_anchor=(1.05, 1), loc=2);
plt.show()


df_uk_cases_1y['dayofyear'] = df_uk_cases_1y['date'].apply(lambda x: x.strftime("%d/%m/%Y"))

df = px.data.wind()

fig = px.line_polar(df_uk_cases_1y, r='cases', theta='dayofyear', start_angle=100+180, direction='counterclockwise',
                    color='areaName', line_close=False,
                    title='Covid-19 case rate per 100.000 people between 1st of June 2020 and 25th of May 2021',
                    width=800, height=800,
                    labels={
                        "casesNormalised": "Rate per 100.000 people ",
                        "dayofyear": "Date",
                        "areaName": "UK nation",
                    },
                    )
fig.update_polars(angularaxis_type="category",radialaxis=dict(visible=True),
angularaxis = dict(
        thetaunit = "degrees",
        dtick =15
      ))


fig.show()




