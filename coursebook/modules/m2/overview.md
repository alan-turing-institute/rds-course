# Module 2 - Handling data (WORK IN PROGRESS!)

TODO: write overview for module 2. Broadly speaking:

- Part 1: Getting and loading data
   - Open data and data sources
   - Licensing, ethics, security.
   - Pandas intro/primer
   - Data formats (CSV, database, API, image, ...) - how to load them into Python with Pandas (mostly).

- Part 2: Exploring and wrangling data
    - Loading a dataset for  the first time (sanity checks, data parsing issues, ...)
    - Manipulating different types of data (text, dates, categorical, images)
    - Feature engineering
    - Missing data
    - Privacy and anonymisation

By the end of this module participants should be able to:
- Load and manipulate tabular data with Pandas.
- Have a high-level understanding of approaches for handling different types of data and preparing them for inclusion in a model or analysis.
- Awareness of the benefits of open data and issues and challenges related to data ethics, security, sensitivity and missing data.

---


inline TODOs:
- `grep "TODO" coursebook/modules/m2/* --exclude=hands-on.ipynb`

outstanding sections:
- FeatureEngineering (in progress)

outstanding subsections:
- sampling bias (not a section in own right?)
    - e.g. collection skewed towards/against single demographic
- badly designed capture/missed variables (e.g. missing q in survey, leading q)
- data storage (perhaps incorporate into data access subsection)?
- Pipelines/best practice for stitching pre-processing together in a reproducible way (and ability to appply pipeline to new data)


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
