---
jupyter:
  jupytext:
    text_representation:
      extension: .md
      format_name: markdown
      format_version: '1.3'
      jupytext_version: 1.10.3
  kernelspec:
    display_name: Python 3 (ipykernel)
    language: python
    name: python3
---

inline TODOs:
- `grep "TODO" coursebook/modules/m2/* --exclude=hands-on.ipynb`

outstanding sections:
- Overview

outstanding subsections (not doing):
- sampling bias (not a section in own right?)
    - e.g. collection skewed towards/against single demographic
- badly designed capture/missed variables (e.g. missing q in survey, leading q)
- data storage (perhaps incorporate into data access subsection)?
- raw data is not raw

outstanding for hands on:
- Hands On
    - handover format?
    
For reference, pandas functions/syntax used in m3/4 I'm not sure we cover in m2 (suggest we ones in bold as those to introduce in M2):
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
