# Privacy and Anonymisation

## Anonymisation or Pseudonymisation 

TODO

removed pending internal discussion


## Differential Privacy

TODO ask Alena to review?

Separate to concerns over data use in developing algorithms, there is also a concern over what may be inferred about the data by learning the result of some randomised algorithm. Here, the concern shifts from intrusion by the data scientist developing the algorithm to the intrusion by the many consumers of this algorithm.

Broadly, differential privacy provides a mechanism for learning nothing about an individual while learning useful information about a population.

> “Differential privacy” describes a promise, made by a data holder, or curator, to a data subject: “You will not be affected, adversely or otherwise, by allowing your data to be used in any study or analysis, no matter what other studies, data sets, or information sources, are available.”

—  *[The Algorithmic Foundations of Differential Privacy](https://www.tau.ac.il/~saharon/BigData2018/privacybook.pdf)* - Dwork & Roth (2014) 

Use of differential privacy in data science and machine learning is an ongoing area of research.

TODO links to recent research?


## References

Dwork, C., & Roth, A. (2014). The algorithmic foundations of differential privacy. Found. Trends Theor. Comput. Sci., 9(3-4), 211-407.