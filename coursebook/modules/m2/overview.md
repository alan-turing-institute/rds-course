# Overview

TODO: write overview for module 2


inline TODOs:
- `grep "TODO" coursebook/modules/m2/* --exclude=hands-on.ipynb`

outstanding sections:
- FeatureEngineering (in progress)

outstanding subsections:
- sampling bias (not a section in own right?)
    - e.g. collection skewed towards/against single demographic
- badly designed capture/missed variables (e.g. missing q in survey, leading q)


outstanding for hands on:
- Extra taught to cover
    - `DataFrame.groupby` - briefly shown in data consistency
    - `Series.str.replace`
    - Selecting rows and columns (`.loc`, `.iloc`, `df[col]`, `df.col`, `df[[col1, col2]]`) - pandas intro, cols and indices, or  data consistency?
- Hands On
    - handover format?
    - fix error reporting in renaming (doesn't handle key error)
    - missing data - e.g. more for some countries than others?


overlaps?:
- Feature Engineering: m3/4?
- Missing Data: m3

Extra thoughts to check we cover:
- raw data is not raw

For reference, pandas functions/syntax used in m3/4 I'm not sure we cover in m2 (don't suggest we attempt to teach many of these though, perhaps ones in bold):
- `df.filter(regex=...)`
- **`df.sort_values(by=column)`**
- **`df["date_column"].dt.xyz`**
- `pd.CategoricalIndex`
- `pd.pivot_table`
- `df.corr()`
- `df[column].isin(values)`
- `df[(df[column]==value1) | (df[column]==value2)]`
- `df.query('column == value')`
- `df.reset_index()`
- `df.size()`
- `df.pivot(x, y, z)`
- **`df[column].apply(myfun)`**
- `df[column].values`


```python

```
