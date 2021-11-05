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

# 2.1.3 Pandas intro

The Pandas library is a core part of the Python data science ecosystem. It provides easy-to-use data structures and data analysis tools.

Pandas has some great resources for getting started, including guides tailored to those familiar with other software for manipulating data: https://pandas.pydata.org/pandas-docs/stable/getting_started/index.html#getting-started .

For now, we'll stick just to what we need for this course.

```{code-cell} ipython3
import pandas as pd
```

## Structures

Pandas has two main **labelled** data structures:
- Series

```{code-cell} ipython3
s = pd.Series([0.3, 4, 1, None, 9])
print(s)
```

- DataFrame

```{code-cell} ipython3
import numpy as np
df = pd.DataFrame(np.random.randn(10,2), index=np.arange(3, 13), columns=["random_A", "random_B"])
df
```

Once we have data in these Pandas structures, we can perform some useful operations such as:
- `info()` - (`DataFrame` only) - prints a concise summary of a `DataFrame`
- `value_counts()` - returns a `Series` containing counts of unique values in the structure

```{code-cell} ipython3
s = pd.Series(np.random.randint(0,2,10))
print(s)
print() # blank line
print("value counts:")
print(s.value_counts())
```

We'll see more on how to use these structures, and other Pandas capabilities, later.

## Indexing

Again, we're just covering some basics here. For a complete guide to indexing in Pandas see [here](https://pandas.pydata.org/pandas-docs/stable/user_guide/indexing.html).

Pandas allows us to use the same basic `[]` indexing and `.` attribute operators that we're used to with Python and NumPy.
However, Pandas also provides the (often preferred) `.loc` labelled indexing method and the `.iloc` position indexing methods.

### `[]` Indexing

For basic `[]` indexing, we can select columns from a DataFrame and items from a Series.

```{code-cell} ipython3
# reusing our DataFrame and Series from earlier

# Basic indexing using `[]` on DataFrame
# select a single column
print("single column from DataFrame, gives us a Series:")
display(df["random_A"])

# select two columns
print("two columns from DataFrame, gives us a DataFrame:")
display(df[["random_A", "random_B"]])

# and for a Series
# select single item
print("single item from Series, gives us an item (of type numpy.int64, in this case):")
display(s[2])

# select two items
print("two items from Series, gives us a Series:")
display(s[[2,4]])
```

Note that we can't do:

```{code-cell} ipython3
:tags: ["raises-exception"]
df[5]
```

as this tries to access a row, not a column.


### Attribute Access

Similarly, we can access a column from a DataFrame and an item from a Series using as an attribute.
However, we can't do this when the label is not a valid identifier. We can't do `s.2`.

```{code-cell} ipython3
:tags: ["raises-exception"]
# Using attribute access
display(df.random_A)
```

```{code-cell} ipython3
:tags: ["raises-exception"]
# and for a Series, this will break
display(s.2)
```

### `.loc`

`.loc` provides label-based indexing. `.loc` can also be used for slicing and we can even provide a `callable` as its input!
However, here we'll just show single item access.

```{code-cell} ipython3
# for DataFrame
display(df.loc[5])

# and for a Series
display(s.loc[2])
```

### `.iloc`

`.iloc` provides integer-based indexing. This closely resembles Python and NumPy slicing. Again, we'll just show single item access.

```{code-cell} ipython3
# for DataFrame
display(df.iloc[5])

# and for a Series
display(s.iloc[2])
```

## String Operations (`Series.str`)

Pandas provides vectorized string functions for Series. Unless explicitly handled, NAs will stay as NA. See [here](https://pandas.pydata.org/docs/reference/api/pandas.Series.str.html).

E.g.
```{code-cell} ipython3
s = pd.Series(["aaa", "aab", "aba"])
# replace "a" with "A"
s.str.replace("a", "A")
```

## Datetime Accessor (`Series.dt`)

Accessor object for datetime-like properties of Series values. See [here](https://pandas.pydata.org/docs/reference/api/pandas.Series.dt.html).

E.g. (taken almost directly from Pandas docs, linked above)
```{code-cell} ipython3
seconds_series = pd.Series(pd.date_range("2000-01-01", periods=3, freq="s"))
display(seconds_series)

# access seconds property of values in series
display(seconds_series.dt.second)
```
