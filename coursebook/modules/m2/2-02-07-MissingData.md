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
# 2.2.7 Missing Data

Missing data often refers to missing values in data, where no data value is stored for a variable or observation.
However, we may also regard missing datasets or data with insufficient disaggregation as a form of missing data.

## Missing Datasets and Insufficient Disaggregation

> "Missing data sets" are my term for the blank spots that exist in spaces that are otherwise data-saturated.

— Mimi Onuoha (2021)

Datasets may not exist, where we might expect them to, for a variety of reasons; these may be political or cultural
 and can be expressive of biases, systematic failures, and/or oppression.

We may also find that, where datasets *do* exist, that the data may not be sufficiently disaggregated to allow for
 analysis that can make issues of inequality apparent. Data may not be broken down by categories such as gender, age, or race,
 preventing the exploration of the impact of these factors on other variables.

```{admonition} Discussion
What considerations would we want to make around publishing disaggregated data for gender, age, and race?
How does this disaggregation fit with [previous discussion](./2-02-LegalityAndEthics.html#should-a-variable-be-used) around use of variables such as race in data analysis?
```

## Missing Data Values

Real world data often has missing values. These may represent gaps in data collection, be expected responses to questions, or be the result of failures or data corruption.

Consider the following question in a survey:
"How many days has it been since your flu jab?"

What answer would you expect from a participant who had not had a flu jab?

### Representing Missing Values


Pandas uses `NaN` (Not a Number) internally to denote missing data, for reasons of computational speed and convenience (beyond our scope!).
However, Python's `None` is also considered a "missing" value and we can check for this with `isna()` or `notna()` methods.

```{margin} .isnull() vs .isna()
These do the same thing!
```

```{code-cell} ipython3
import pandas as pd
pd.Series([None,"foo","bar"]).isnull()
```

Pandas has some other ways of denoting missing values, but we won't detail them here. A more complete guide to missing data in Pandas can be found in the [docs](https://pandas.pydata.org/pandas-docs/stable/user_guide/missing_data.html).


### Dealing with Missing Values

How do we deal with missing values? There are many approaches, we outline two simple and popular varieties below:

#### Listwise Deletion

Simply drop any rows that contain missing values. This is the simplest method of dealing with missing data!

However, this can introduce bias. We should consider *why* the data is missing.
Listwise deletion will introduce bias when the remaining data can no longer be reflective of the original data.

#### Single Imputation

Apply a rule to replace a missing value. For example, replace with the mean or the value of the last observation (last observation carried forward - LOCF).

Again, single imputation methods can easily introduce bias. Use with caution.

### Missingness Terminology

Here, we introduce some terminology to help us with the scenarios in which values are missing.

[Sterne et al. (2009)](https://www.bmj.com/content/338/bmj.b2393/) provide similar definitions with biomedical examples and discussion of the use of multiple imputation.

#### Missing Completely At Random (MCAR)

The missingness is unrelated to both missing and observed values, e.g., a study participant's weekly questionnaire is lost in the post.

If we were to drop rows with MCAR data, we would reduce our population size but would not introduce any bias.

Unfortunately, missing values are rarely MCAR.

Note that, whilst we can falsify the hypothesis that data are MCAR, we cannot confirm it.

#### Missing At Random (MAR)

Slightly confusingly named, in MAR data missingness is related to observed data but not the missing values themselves,
e.g., a person does not attend an academic exam because they are too unwell to travel **and** we also have their health records.

MAR data allows the prediction of missing values based on complete rows. However, as ever, imputation should be approached with caution!

Classification of missing data as MAR should be done with care and will rely on domain knowledge.

#### Missing Not At Random (MNAR)

The missingness is related to what is missing, e.g., a person does not attend a health assessment because they are too unwell to travel.

When data is MNAR no methods exist to handle this missingness appropriately (Sterne et al. 2009).

**We cannot test whether data is MAR vs MNAR as the data required is missing**.

## References

Mimi Onuoha. (2021). On Missing Data Sets. https://github.com/MimiOnuoha/missing-datasets (Original work published 2016)

Sterne, J. A., White, I. R., Carlin, J. B., Spratt, M., Royston, P., Kenward, M. G., ... & Carpenter, J. R. (2009). Multiple imputation for missing data in epidemiological and clinical research: potential and pitfalls. Bmj, 338.
