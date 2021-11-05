# 2.2.3 Feature Engineering

- what
- why

```{note}
This section focuses on numerical data, we discuss approaches for other types in later sections. 
```

The Anthropometric Survey of US Army Personnel ([ANSUR 2](https://www.openlab.psu.edu/ansur2/)) dataset.

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

```{note}
It's also an interesting example of data documentation, with over 250 pages of notes on how the measurements were taken in its [Measurer’s Handbook](http://tools.openlab.psu.edu/publicData/ANSURII-TR11-017.pdf), for example.
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
log_age = np.log(df["Age"])

plt.hist(log_age, bins=20)
plt.title("Age: Log Transformed")
```

## Creating New Features

Another common task is to use domain knowledge to create new features that may be of interest for an analysis, or could add predictive power to a model. For this dataset it may be useful to compute the body mass index of the army personnel, for example, the formula for which is:

$$
\textrm{BMI} = \frac{\textrm{weight}}{\textrm{height}^2}
$$

with weight in kilograms and height in metres. It's quick to do this with Pandas:

```python
df["bmi"] = df["weightkg"] / df["stature"]**2
df["bmi"].describe()
```

As well as curating domain-specific features, another option is to generate many possible combinations of the original columns, and then perhaps select a subset of promising ones after further analysis (see feature selection below). The [`PolynomialFeatures`](https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.PolynomialFeatures.html#sklearn.preprocessing.PolynomialFeatures) class in the scikit-learn library generates features that are polynomial combinations of the original features (`weight`, `height`, `weight^2`, `height^2`, `weight * height`, ...), for example.

To apply an arbitrary function to a data frame Pandas you can also use [`apply`](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.apply.html):

```python
def calculate_bmi(person):
    """Calculate body mass index from  a person's data.
    Person is a pandas series which must include 'weightkg' and 'stature' in its index."""
    return person["weightkg"] / person["stature"] ** 2


df.apply(calculate_bmi, axis=1)
```

```{note}
With `axis=1` the function will be applied to each row in the data frame, or with `axis=0` to each column.
```

`apply` works like using a `for` loop on the data, which means it doesn't benefit from the optimised vector operations `numpy` provides: 

```python
%%timeit

df.apply(calculate_bmi, axis=1)
```

```python
%%timeit

df["weightkg"] / df["stature"]**2
```

Using `apply` is almost two hundred times slower (the exact ratio will vary depending on your system), and for larger datasets or more complex functions this can add up to a lot of time! We cover ways to make Python code run faster in more detail in the "Programming for Speed" module of our [Research Software Engineering course](https://github.com/alan-turing-institute/rsd-engineeringcourse), but it's better to avoid using `apply` if you can.

Which columns and functions to use and combine into new features is problem-specific and there's no one-size-fits-all solution.


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

It's beyond the scope of what we cover here, but another important topic is the "curse of dimensionality", or what to do when we have many features (columns) relative to the number of samples (rows) in the dataset. [This blog post](http://blog.dominodatalab.com/the-curse-of-dimensionality) summarises how this can cause problems in some models.

- Feature selection: 
- Dimensionality reduction: https://en.wikipedia.org/wiki/Principal_component_analysis https://scikit-learn.org/stable/modules/decomposition.html#pca
- Regularization: https://programmathically.com/regularization-in-machine-learning/



## Other

- correlated features
- outliers??
- pipelines

```python
[print(c) for c in df.columns];
```
