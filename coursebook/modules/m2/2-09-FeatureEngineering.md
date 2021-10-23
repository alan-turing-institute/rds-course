# 2.9 Feature Engineering

- what
- why

```{note}
This section focuses on numerical data, but we discuss approaches for other types in later sections. 
```



```python
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
```

```python
df = pd.read_csv("data/ANSUR_II_FEMALE_Public.csv")
df.info()
df.head()
```

## Scaling & Transforming Features

- when/why

### Converting Units

Despite the name, the `weightkg` column is in units of 100 grams, or tenths of a kilogram:

```python
df["weightkg"].describe()
```

And the `stature` (the person's height) column is in millimetres:

```python
df["stature"].describe()
```

For interpreting the data ourselves and presenting it to other it's helpful to have values on scales we're familiar with. It's quick to perform simple mathematical operations on columns with Pandas - let's convert the `weightkg` column to actually be in kilograms, and the `stature` column to be in metres:

```python
df["weightkg"] = df["weightkg"] / 10  # 100g -> kg
print("Median weight:", df["weightkg"].median(), "kg")

df["stature"] = df["stature"] / 1000  # mm -> metres
print("Median height:", df["stature"].median(), "m")
```

These look more familiar (at least if you're used to using the metric system!) We can also see that women in the army are lighter and taller on average compared to the general population ([73.1 kg median weight and 1.613 metres median height](https://www.cdc.gov/nchs/data/series/sr_03/sr03-046-508.pdf)), so we'd need to be careful not to generalise results from this data to the USA as a whole.


### Normalization

- min-max, others ...

```python
def get_stats(series):
    """Get a formatted message with the minimum, maximum, mean, and
    standard deviation of a pandas series"""
    return "min = {:.2f}, max = {:.2f}, mean = {:.2f}, std = {:.2f}".format(
        series.min(),
        series.max(),
        series.mean(),
        series.std(),
    )


columns = ["anklecircumference", "axillaheight"]

print("Original:")
for col in columns:
    print(col, ":", get_stats(df[col]))

```

```python
def norm_min_max(series):
    """Min-max scale a pandas series"""
    return (series - series.min()) / (series.max() - series.min())


print("Min-max scaled:")
for col in columns:
    df[col] = norm_min_max(df[col])
    print(col, ":", get_stats(df[col]))

```

### Standardization

- mean 0 std 1,

```python
def standardize(series):
    """Standardize a pandas series to have zero mean and unit
    standard deviation"""
    return (series - series.mean()) / series.std()


columns = ["footlength", "earlength"]

print("Original:")
for col in columns:
    print(col, ":", get_stats(df[col]))

print("\nStandardized:")
for col in columns:
    df[col] = standardize(df[col])
    print(col, ":", get_stats(df[col]))

```

### Transformation

- when/why
- types

```python
df["Age"].plot.hist(bins=20)
plt.title("Age: Original")
```

```python
plt.hist(np.log(df["Age"]), bins=20)
plt.title("Age: Log Transformed")
```

## Creating New Features



```python
df["bmi"] = df["weightkg"] / df["stature"]**2
df["bmi"].describe()
```

Link to higher order (polynomial) features


## Binning

- make things categorical
- when/why (including privacy/anonymisation)

```python
df["span"].plot.hist(bins=20)
```

Pandas provides a binning function [`pd.cut`](https://pandas.pydata.org/docs/reference/api/pandas.cut.html), which by default segments the data into a number of of equal-width bins:

```python
span_bins = pd.cut(df["span"], 10)
span_bins
```

This returns a Pandas series with a "category" data type (see [here](https://pandas.pydata.org/pandas-docs/stable/user_guide/categorical.html) for more information). Each value in the data is assigned to the bin (or category) whose range encompasses it, with each bin labelled as `(minimum value, maximum value]`.

Rather than the verbose bin label, you can also extract a bin index (ranked from smallest to largest) using the `.cat.codes` attribute:

```python
span_bins.cat.codes
```

We talk more about categorical data in Section 2.11. Pandas also provides an alternative binning function, [`pd.qcut`](https://pandas.pydata.org/docs/reference/api/pandas.qcut.html), which creates bins based on quantiles. In this case each bin contains approximately the same proportion of the data (but the bins have differrent widths):

```python
span_qbins = pd.qcut(df["span"], 4)
span_qbins.value_counts(sort=False)
```

## Feature Selection and Dimensionality Reduction

```python

```

## Other

- correlated features
- outliers??
- pipelines

```python
[print(c) for c in df.columns];
```
