# 2.1.1 Where to find data?



## What is Open Data?

We can use the definition from [The Turing Way](https://the-turing-way.netlify.app/reproducible-research/open/open-data.html): Open data is freely available on the internet. Any user is permitted to download, copy, analyse, re-process, and re-use it for any other purpose with minimal financial, legal, and technical barriers.

The benefits of using an open dataset include (but are not limited to):

- Access to the data is free and usually fast (without requiring a registration/approval process).
- Other researchers may have used the same dataset and published guidelines, code and other details about the dataset that are also in the public domain. So we can benefit and draw inspiration from their prior work.
- Transparency & reproducibility: If the dataset we're using is open we can make all our research (data, code & publications) open as well, so others can easily reproduce and contribute to our work.

[The Open Data Handbook](https://opendatahandbook.org/guide/en/why-open-data/) has a longer discussion of the benefits of open data.

Even if a dataset is public, we must still evaluate whether it is ethical to use it and its licensing/legal requirements - not all public datasets are completely "open"!

## Sources of Open Data

There are many sources of data online, below are a few ideas for places to look.

### Tailored for Data Science

Provide datasets with data science applications in mind, so are more likely to be in easy-to-use formats and may have already been pre-processed in some way. Many popular machine learning libraries like PyTorch also have datasets built in. These are excellent sources for finding datasets to learn, test and benchmark algorithms or other analysis techniques, but are less likely to be rich sources for novel research projects.

  - [Kaggle](https://www.kaggle.com/datasets)
  - [UCI Machine Learning Repository](https://archive.ics.uci.edu/ml/index.php)
  - [Google research](https://research.google/tools/datasets/)
  - [scikit-learn](https://scikit-learn.org/stable/datasets/toy_dataset.html), [Tensorflow](https://www.tensorflow.org/datasets), [PyTorch](https://pytorch.org/vision/stable/datasets.html)


### Countries/Governments

Many governments commit to publishing data in the open for public interest and transparency. The datasets might be less "data science ready", but they cover a broad range of topics.

- UK:
  - [data.gov.uk](https://data.gov.uk/)
  - [UK Data Service](https://www.ukdataservice.ac.uk/)
  - [Office for National Statistics (ONS)](https://www.ons.gov.uk/)

- Other countries/regions:
  - [data.gov](https://www.data.gov/) (USA)
  - [data.europa.eu](https://data.europa.eu/en) (EU)
  - [africaopendata.org](https://africaopendata.org/) (Africa)
  - [dataportal.asia](https://dataportal.asia/home) (Asia)

### Organisations

Large humanitarian organisations often make data available, such as:

  - [World Bank](https://microdata.worldbank.org/index.php/home)
  - [World Health Organisation](https://www.who.int/data/collections)
  - [International Monetary Fund](https://www.imf.org/en/Data)


### General

General tools and repositories that contain data across many different domains:

   - [Google Dataset Search](https://datasetsearch.research.google.com/)
   - GitHub: Although large datasets can't be stored on GitHub there are many smaller datasets to be found in GitHub repositories. There are also community-maintained lists of interesting datasets, e.g., [awesome-public-datasets](https://github.com/awesomedata/awesome-public-datasets).
   - [Zenodo](https://zenodo.org/): Combined repository for open data, papers, and code.
   - [FAIRsharing](https://fairsharing.org/): A catalogue of databases across many  different domains.



## When Open Data Isn't Available

If you can start your project with an open dataset that's always preferable. Even if the perfect dataset is not openly available it may be worth first prototyping with related data that is open. For example, it may be that an older version of the data you're interested in has been made public. You can continue to explore options for getting the ideal data in parallel, but gaining data access is frequently an expensive or time-consuming process.

Two common reasons open data may not be available or appropriate are 1) the data is commercially sensitive or valuable, and 2) the data presents a privacy or security risk. Access to detailed healthcare records, for example, is often heavily restricted even if personal identifiers have been removed due to the risk of re-identification. In August 2016 the Australian government openly published a de-identified medical billing dataset, but one month later [researchers at the University of Melbourne](https://arxiv.org/pdf/1712.05627.pdf) demonstrated it was possible to re-identify individuals and the data was taken offline.

Options for finding a non-open dataset include:

### Ask!

Although open data may not be available for your project, a collaborator, someone else at your institute, company, or the wider community could have something relevant. However, even if they're willing to share it, you must check what the conditions are for access and usage of the data and get advice where necessary. Always err on the side of caution, especially if any of the data relates to living individuals. Alternatively, you may find someone else that's interested in the same data, and you could join forces (or budgets) to get it.

### Paywalled/Restricted Access

Getting access to a dataset that's behind closed doors is likely to involve a registration or application process and may include a fee. Bear in mind that data can be _expensive_, and could easily cost thousands of pounds, for example. If the application is approved, the resulting contract/ research agreement may specify precisely which data you can have access to (down to the level of individual fields), who will have access, the duration of access, and exactly what you're allowed to do with it. As an example, [this website](https://www.ukbiobank.ac.uk/enable-your-research) describes the process for accessing the UK Biobank, a large biomedical database for health research.

### Creating Your Own Dataset

Ultimately the data you need might not be available anywhere, in which case the only option could be to collect it yourself. Designing datasets is not the focus of this course, but if you're making your own remember you'll be the one analysing it! Investing time in thinking about how your data will be structured and how you'll deal with missing values and the many other issues common in datasets will save a lot of time later. You must also carefully consider whether it is ethical to collect the data and have approval from your organisation to do so.



<!-- #region -->
## Assessing Dataset Quality and Suitability

TODO

In Module 1 (Section 1.2, question 3 for scoping projects) we gave these overarching questions for evaluating a dataset:
- Does the dataset contain what's needed to solve the research question available?
- Can I legally and ethically use the data?
- Is the data easily accessible?
- Is the dataset well-understood and tested?
- Is data quality and quantity appropriate?


Another useful concept here is [data readiness levels](https://arxiv.org/pdf/1705.02245.pdf):
- A
- B
- C

<!-- #endregion -->

## Data Attached to a Research Project

TODO

- how to and advocating for making data open
- open versions of sensitive data

FAIR principles

https://the-turing-way.netlify.app/reproducible-research/rdm/rdm-sharing.html#rr-rdm-sharing
