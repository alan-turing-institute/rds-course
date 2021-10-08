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

#  2.7 Modifying Columns and Indices


## Dropping Named Columns and Indices

We may wish to drop columns or indices entirely from a Pandas DataFrame. 

This may be where we've already done some analysis and know the labels of the column(s) to drop.
We use the [`DataFrame.drop`](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.drop.html) method:

```{code-cell} ipython3
from IPython.display import display

import pandas as pd
import numpy as np

# construct df with null values
df = pd.DataFrame.from_dict({
    "col_a": [1, 2, np.nan, 4],
    "col_b": ["aaa", "bbb", "ccc", "ddd"],
    "col_c": ["AAA", "BBB", "CCC", None],
    "col_d": [np.nan, np.nan, np.nan, np.nan],
})

# show the dataframe
print("original dataframe:")
display(df)

print("drop 'col_b':")
display(df.drop(columns=["col_b"]))
```

We can also use this method to drop indices:

```{code-cell} ipython3
# show the dataframe
print("drop rows 1 and 3")
display(df.drop(index=[1,3]))
```

## Dropping Columns and Indices With Nulls

It may be that we wish to drop columns according to whether they have missing data.
Here, we use the [`DataFrame.dropna`](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.dropna.html) method:

```{code-cell} ipython3
# show the dataframe
print("original dataframe recap:")
display(df)

print("drop columns where *all* values are NA:")
display(df.dropna(axis="columns", how="all"))

print("drop columns where *any* values are NA:")
print("note that None is treated like NaN.")
display(df.dropna(axis="columns", how="any"))
```

Once again, we can use this method to drop indices:

```{code-cell} ipython3
print("drop rows where any of  'col_a', 'col_b', 'col_c' are NA:")
display(df.dropna(axis="index", how="any", subset=["col_a", "col_b", "col_c"]))
```

## Relabelling Columns and Indices

Sometimes we'll be dealing with data that is inconveniently named.

Pandas provides an easy way to rename columns:

```{code-cell} ipython3
df = pd.DataFrame({"long_column_name": [1, 2, 3], "short": [4, 5, 6]})
print("original df:")
display(df)
df = df.rename(columns={"long_column_name": "long"})
print("renamed df:")
display(df)
```

We can also modify indices in this fashion.

```{code-cell} ipython3
print("original df:")
display(df)
df = df.rename(index={0: 10})
print("renamed df:")
display(df)
```

TODO: maybe these (and some of the above) are overkill unless needed in hands on?:
 - `set_index` ?
 - `reset_index` ?
