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
# 2.2.6 Linking Datasets

Data linking is the process of joining datasets together.
Datasets can be useful on their own but bringing them together can unlock new insights. 

```{admonition} Discussion
When might this be helpful? Can you think of any examples where joining datasets might help us unlock additional insights?
``` 

## Impact on Privacy

Before we link datasets together, we should consider the impact on privacy of doing so. 
There can be an increased risk of identification of a person/entity when two datasets are linked.

 
## How to Link

The most straightforward way to link datasets is by a deterministic, rules based linkage, where records are linked if a specific **set of identifiers** match.
When working with tabular datasets we will often see this accomplished with a *join* operation.

### Joining in Pandas

Pandas allows for database-style joins. If you have experience of SQL you'll be familiar with the terminology of left/right/inner/outer etc. joins.
Pandas makes these join types (or similar) available in the Pandas API via with `pd.merge` and provides a comprehensive summary of joins [in the docs](https://pandas.pydata.org/docs/user_guide/merging.html#database-style-dataframe-or-named-series-joining-merging).
Here, for demonstration, we will give an example using a simple left join, similar to a `LEFT OUTER` join in SQL. 

```{code-cell} ipython3
import pandas as pd

df1 = pd.DataFrame({'some_id': ['foo', 'bar', 'zop'], 'a': [0,1,2]})
df2 = pd.DataFrame({'some_id': ['foo', 'bar', 'baz'], 'b': [3, 4, 5]})

print("df1")
display(df1)

print("df2")
display(df2)
```

note that `df1` contains the key `'zop'` that is not contained in `df2` and that `df2` contains the key `'baz'` that is not contained in `df1`.
The other two keys, `'foo', 'bar'` are contained in both dataframes.

```{code-cell} ipython3
result = pd.merge(left=df1, right=df2, how="left", on="some_id")
display(result)
```

the data for `'baz'` has been dropped after this join as it only appeared on the 'right' side.
The `how='left'` join only uses keys from the left frame.
Meanwhile, the entry for column `'b'` is a null for key `'zop'`.  

Different scenarios will require different join types, read the docs carefully! 

### Probalistic Matching

If we don't have a set of common identifiers, we may wish to use probabilistic matching.

Probabilistic matching calculates a matching score between two records.
Typically, this is done by comparing several field values and assigning a weight to each depending on how closely they match.

Details of probabalistic matching approaches are, unfortunately, beyond the scope of this course.  