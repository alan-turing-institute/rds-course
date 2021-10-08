---
jupytext:
  cell_metadata_filter: -all
  formats: md:myst
  text_representation:
    extension: .md
    format_name: myst
    format_version: 0.13
    jupytext_version: 1.10.3
kernelspec:
  display_name: Python 3 (ipykernel)
  language: python
  name: python3
---
# 2.15 Missing Data

Missing data often refers to missing values in data, where no data value is stored for a variable or observation.
However, we may also regard missing datasets or data with insufficient disaggregation as a form of missing data.

## Missing Datasets and Insufficient Disaggregation

> "Missing data sets" are my term for the blank spots that exist in spaces that are otherwise data-saturated.

— Mimi Onuoha (2021)

Datasets may not exist, where we might expect them to, for a variety of reasons; these may be political or cultural
 and are can be expressive of biases, systematic failures, and/or oppression.

We may also find that, where datasets do exist, that the data may not be sufficiently disaggregated to allow for
 analysis that can make issues of inequality apparent. Data may not be broken down by categories such as gender, age, or race, 
 preventing the exploration of the impact of these factors on other variables.

```{admonition} Discussion
What considerations would we want to make around publishing disaggregated data for gender, age, and race?
``` 

## Missing Data Values

Real world data ofen has missing values. These may represent gaps in data collection, be expected responses to questions, or be the result of failures or data corruption.

Consider the following question in a survey:
"How many days has it been since your flu jab?"

What answer would you expect from a participant who had not had a flu jab? 

### Representing Missing Values


Pandas uses `NaN` (Not a Number) internally to denote missing data, for reasons of computational speed and convenience (beyond our scope!).
However, Python's `None` is also considered a "missing" value and we can check for this with `isna()` or `notna()` methods.

```{code-cell} ipython3
import pandas as pd
pd.Series([None,"foo","bar"]).isna()
```

Pandas has some other ways of denoting missing values but we won't detail them here. A more complete guide to missing data in Pandas can be found in the [docs](https://pandas.pydata.org/pandas-docs/stable/user_guide/missing_data.html).


### Dealing with Missing Values

TODO

- Dealing with missing values:
    - imputation
    - delete/ignore/drop

### Missingness Terminology

Some terms to help us with the scenarios in which values are missing:

#### Missing Completely At Random (MCAR)

The missingness is unrelated to both missing and observed values, e.g. a study participant's weekly questionnaire is lost in the post.

If we were to drop rows with MCAR data, we would reduce our population size but would not introduce any bias. 

Unfortunately, missing values are rarely MCAR.

#### Missing At Random (MAR)

TODO: better example
TODO: dropping/imputation

Slightly confusingly named, in MAR data missingness is related to observed data but not the missing values themselves,
e.g. a person does not attend an academic exam because they are too unwell to travel and we also have their health records.


#### Missing Not At Random (MNAR)

The missingness is related to what is missing, e.g. a person does not attend a health assessment because they are too unwell to travel.

TODO: dropping/imputation

## References

Mimi Onuoha. (2021). On Missing Data Sets. https://github.com/MimiOnuoha/missing-datasets (Original work published 2016)
