# 2.2.5 Privacy and Anonymisation

This section touches, again, on UK GDPR. A comprehensive guide to UK GDPR can be found on the [ICO website](https://ico.org.uk/for-organisations/guide-to-data-protection/guide-to-the-general-data-protection-regulation-gdpr/).

## Anonymisation or Pseudonymisation 

Pseudonymisation and anonymisation are common approaches to meet GDPR principles of ["data minimisation" and "storage limitation"](https://www.privacy-regulation.eu/en/article-5-principles-relating-to-processing-of-personal-data-GDPR.htm). 

Many tasks do not require the use of personal identifiers that can often be part of a dataset. In these cases, we should aim to remove this unnecessary, yet sensitive, data.

### Anonymisation 

In a GDPR context, Recital 26 defines anonymous information as:
> …information which does not relate to an identified or identifiable natural person or to personal data rendered anonymous in such a manner that the data subject is not or no longer identifiable.

— *[Recital 26](https://www.privacy-regulation.eu/en/recital-26-GDPR.htm)*

Anonymisation is the process of removing direct and indirect personal identifiers. Crucially, post-anonymisation, subjects will not be able to be identified in the data, even given additional information.

GDPR does not apply to anonymised information. However, note that when **you** anonymise personal data, **you** are still processing the data at that point.


### Pseudonymisation

> …the processing of personal data in such a manner that the personal data can no longer be attributed to a specific data subject without the use of additional information, provided that such additional information is kept separately and is subject to technical and organisational measures to ensure that the personal data are not attributed to an identified or identifiable natural person.

—  *excerpt from [ICO Guide to Data Protection](https://ico.org.uk/for-organisations/guide-to-data-protection/guide-to-the-general-data-protection-regulation-gdpr/what-is-personal-data/what-is-personal-data/#pd4)*

This is subtly different to anonymisation. Here, the subject can be re-identified, given additional information.

GDPR does still apply to pseudonymised information. However, this still helps meet the "data minimisation" and "storage limitation" principles.


## Differential Privacy

Separate to concerns over data use in developing algorithms, there is also a concern over what may be inferred about the data by learning the result of some randomised algorithm. Here, the concern shifts from intrusion by the data scientist developing the algorithm to the intrusion by the many consumers of this algorithm.

Broadly, differential privacy provides a mechanism for learning nothing about an individual while learning useful information about a population.

> “Differential privacy” describes a promise, made by a data holder, or curator, to a data subject: “You will not be affected, adversely or otherwise, by allowing your data to be used in any study or analysis, no matter what other studies, data sets, or information sources, are available.”

—  *[The Algorithmic Foundations of Differential Privacy](https://www.tau.ac.il/~saharon/BigData2018/privacybook.pdf)* - Dwork & Roth (2014) 

Use of differential privacy in data science and machine learning is an ongoing area of research. 
We recommend the 2018 blog post, [Privacy and machine learning: two unexpected allies?](http://www.cleverhans.io/privacy/2018/04/29/privacy-and-machine-learning.html), as further reading.


## References

Dwork, C., & Roth, A. (2014). The algorithmic foundations of differential privacy. Found. Trends Theor. Comput. Sci., 9(3-4), 211-407.
