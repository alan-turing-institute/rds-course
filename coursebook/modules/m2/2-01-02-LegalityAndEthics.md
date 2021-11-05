# 2.1.2 Legality and Ethics


Before we dive into using any dataset, we need to consider who **owns** the data that we wish to use and what **restrictions** they or regulatory/governing bodies may have put in place.
We must also consider the ethical implications of using the dataset.

## Legality

**Important disclaimer: we are not legal experts, and this is not legal advice. 
The content in this section is non-exhaustive, based on our personal experiences, and is aimed at making you aware of these issues.
Check your university/employer’s policies for guidance. If in any doubt, speak to an expert.**

### Licences

> A licence agreement is a legal arrangement between the creator/depositor of the data set and the data repository, signifying what a user is allowed to do with the data. 

—  *[The Data Management Expert Guide by CESSDA ERI](https://www.cessda.eu/Training/Training-Resources/Library/Data-Management-Expert-Guide)*

As a user, it is your responsibility to abide by the terms of a licence when making use of a dataset. This is similar to licensing for software.

```{margin} Open Data
> Open data is data that can be freely used, re-used and redistributed by anyone – subject only, at most, to the requirement to attribute and sharealike.

— [Open Data Handbook](http://opendatahandbook.org/guide/en/what-is-open-data/)
```

Licences range in the freedoms they give to users. Licences that grant users freedoms over (re)use and (re)distribution are *permissive*. Some common examples are:

 - [Creative Commons Attribution 4.0 International (CC BY 4.0)](https://creativecommons.org/licenses/by/4.0/)
     - the dataset may be shared and adapted as long as credit is given, the original is linked, and any changes are noted.
 - [CDLA-Sharing-1.0](https://cdla.io/sharing-1-0/)
     - a "copy-left" license. Similar restrictions to CC BY 4.0 but you must use the same license if resharing the data (or "enhanced data"). Importantly, restrictions **do not** apply to results of computational use.  


However, not all licences give so many freedoms. It's always worth checking.

```{warning}
All open source/open access licensed materials are provided as-is. Use with caution.
```

```{admonition} Research vs non-Research
Some licenses will grant permission for *research only*. There is a blurred line on what may constitute research vs non-research.
We suggest that you check internally with your organisation. This determination can change depending on the nature of the work; this is especially important to remember if your time is split over multiple projects.
``` 

**NB**: GitHub's default stance for [no licence](https://choosealicense.com/no-permission) being present is that the work is under exclusive copyright by default.

More information on data licences can be found in [The Turing Way](https://the-turing-way.netlify.app/reproducible-research/licensing/licensing-data.html).


### Data Protection & GDPR

> The Data Protection Act 2018 is the UK’s implementation of the General Data Protection Regulation (GDPR).
> 
> Everyone responsible for using personal data has to follow strict rules called ‘data protection principles’. They must make sure the information is:
> 
> - used fairly, lawfully and transparently
> - used for specified, explicit purposes
> - used in a way that is adequate, relevant and limited to only what is necessary
> - accurate and, where necessary, kept up to date
> - kept for no longer than is necessary
> - handled in a way that ensures appropriate security, including protection against unlawful or unauthorised processing, access, loss, destruction or damage
> 
> There is stronger legal protection for more sensitive information, such as:
> 
> - race
> - ethnic background
> - political opinions
> - religious beliefs
> - trade union membership
> - genetics
> - biometrics (where used for identification)
> - health
> - sex life or orientation
> 
> There are separate safeguards for personal data relating to criminal convictions and offences.

—  *excerpt from https://www.gov.uk/data-protection*

Note: The DPA 2018 sits alongside and supplements [UK GDPR](https://www.legislation.gov.uk/eur/2016/679/contents).

#### What's personal data?

Personal data is information about a particular living individual. It doesn't need to be "private" information.

Truly anonymous information isn't covered - but if you could use the data to identify someone (e.g., by combining it with another source) it still counts as personal data.

Summarised from: https://ico.org.uk/for-organisations/guide-to-data-protection/introduction-to-data-protection/some-basic-concepts/

See more at: https://ico.org.uk/for-organisations/guide-to-data-protection/guide-to-the-general-data-protection-regulation-gdpr/key-definitions/what-is-personal-data/

#### Does it apply to me?

> The law applies to any ‘processing of personal data’, and will catch most businesses and organisations, whatever their size.

—  *excerpt from [ICO Guide to Data Protection](https://ico.org.uk/for-organisations/guide-to-data-protection/introduction-to-data-protection/some-basic-concepts/?q=apply+to+me#2)*

However, there are a few exemptions to GDPR and some things that are simply outside its scope.

Personal or household activities are considered outside of the scope of the UK's GDPR. Data **only** for personal use won't make  you subject to GDPR.

Crucially, for academia and research, there are some exemptions. The details of these can be complicated and are certainly beyond the scope of this course. Each organisation will have their own stance on GDPR, and you should consult internally to determine how to proceed.


For exemptions, see: https://ico.org.uk/for-organisations/guide-to-data-protection/guide-to-the-general-data-protection-regulation-gdpr/exemptions/


### Commercial agreements

Research projects are often collaborative efforts that may span multiple organisations. Commonly, these collaborations take place under some defined commercial agreement (a contract). Such an agreement may impact on your use of data.

For example:

*VacuumOrg have a contract with your organisation, DullResearchInc, to conduct research into consumer spending on robot vacuum cleaners. As part of this research, MarketingOrg have shared some survey data with you that they have collected over the last 6 months. The data collection was expensive, and the data is considered hot property by MarketingOrg; they don't wish their competitors to have access to it and only share it with you under a Non-Disclosure Agreement (NDA).*

*You want to transfer the data (5Mb) from your colleagues PC to your work laptop. Assuming some oddly limited options, which of the following do you do?*
-  *A. upload it to your public GitHub repository so you can pull it down later*
-  *B. transfer via a DullResearchInc USB stick*


## Ethics

**Ethics are a shared responsibility, however, it's another area that we should all feel comfortable seeking expert advice. At Turing, we have an Ethics Advisory Board that we can look to for guidance.**


Although there will be a lot of crossover between legality and ethics, we should be aware that there may be additional ethical considerations over use of a dataset, even when its use is deemed legal.


For example:

*The UK data service lists the European Quality of Life Time Series, 2007 and 2011: Open Access dataset available for download and use under a CC BY 4.0 licence.
As the data do not contain direct personal identifiers, and it is unlikely that anyone will be able to identify individuals, we are confident that, from a data protection angle, we can proceed.

*However, we may wish to consider the consent under which this data was originally gathered. Did the respondees to this survey explicitly consent to its secondary use in research (or teaching, in this case)? If not, can we assume implied consent? Do we need consent at all, in this case?*

> We believe that despite the lack of an explicit consent field in the questionnaire, these materials and all the supporting material in the website give plenty of information and signposting to participants to assure that they know the content and purpose of the survey, the anonymisation process, the way data will become available and also to know where to ask questions if they have concerns.
> It is reasonable to conclude that participants that were contacted, accepted the invitation, read this material, were briefed by the field worker and went ahead with the interview did consent to their data being collected and used.
> It is also clear that during this process they had the option to opt out more than once.
> The type of intended research is not made entirely clear from the forms but there are mentions to improving living conditions in Europe, understanding quality of life and also other examples of uses in the 2007 flyers. 

— *excerpt from Ethics Advisory Group practice application form submitted for the running this course*

The above excerpt is part of a larger document that outlines our application to Turing's Ethics Advisory Group.
The decision to move forward with the dataset was made given consideration of the paragraph quoted as well as points set
 out in the rest of the document. 

### Bias in, bias out

We should also consider *how* and *why* the data was collected. Is it suitable for use in our project?
Would use of this data lead us to a "bias in, bias out" situation with any resulting model?

2018 reports of a recruiting tool at Amazon highlight a great example of this idea.

> .. But by 2015, the company realized its new system was not rating candidates for software developer jobs and other technical posts in a gender-neutral way.
>
>That is because Amazon’s computer models were trained to vet applicants by observing patterns in resumes submitted to the company over a 10-year period. Most came from men, a reflection of male dominance across the tech industry.
>
>In effect, Amazon’s system taught itself that male candidates were preferable. It penalized resumes that included the word “women’s,” as in “women’s chess club captain.” ...

— *excerpt from [Reuters article "Amazon scraps secret AI recruiting tool that showed bias against women"](https://www.reuters.com/article/us-amazon-com-jobs-automation-insight-idUSKCN1MK08G)*

#### Beyond Data

The idea of "bias in, bias out" may be concerned with more than simply the data that is used.
Overarching systems, as well as programmers themselves, can contribute to this cycle, such as explored in Mason (2018) and Cowgill et al. (2020).


### Should A Variable Be Used?

Questions of ethics don't necessary stop at the dataset level. Once we have access to a dataset, we can examine the variables that are recorded in the data.

Use of machine learning techniques in domains such as criminal justice, insurance, and financial credit raise concerns about fairness.
These techniques often rely on historic data, containing historic biases against demographic groups, and can perpetuate these biases into their predictions (bias in, bias out!).
Clearly, decisions made based on these predictions may be unfair. We may wish to address this by excluding demographic variables from the training data.

Our concern here isn't limited to machine learning, however.
In biomedical research, for example, there is [debate](https://www.publichealthpost.org/research/why-are-we-still-using-race-as-a-variable-in-health-research) around the use of race as a variable in data analysis. 
Yudell et al. (2020) argue that, in COVID-19 analysis, reported disparities in cases across racial demographics can give rise to false beliefs that the disparities are caused by innate racial differences.

We'll revisit this from another angle in [2.15 Data Missingness](./2-15-MissingData.md).

### Data Proxies

We should also be aware that a variable `Y` may act as proxies for another variable `X` and, in doing so, lead to the inclusion of a variable that we may have intended to drop.

>For example, suppose a system that makes decisions about credit uses zip code as a factor to make its decisions.
> The direct information about race is not given to the system, but zip code is strongly correlated with race since many neighborhoods are still segregated.
> By using zip code, the system would be indirectly making decisions based on race. In this case, zip code is a proxy for race.

—  *[Thwarting bias in AI systems](https://engineering.cmu.edu/news-events/news/2018/12/11-datta-proxies.html)*

We can try to identify proxy variables by looking at data correlations and asking domain experts.

### Algorithmic Fairness: A Trade-off
 
Many works exist in the area of algorithmic fairness, and this is a topic worthy of greater discussion outside of the boundary of this course.
Here, we want to briefly highlight a tension between fairness and traditional measures of performance.

Above, we have discussed excluding variables from the data.
When we have a modelling task, we may find that our reported accuracy is lower without our excluded variables. This represents a trade-off.
We should attempt to discern the implications of the change in accuracy and potentially consider these against measures of fairness.

But what is "fairness"? Any answer is certainly beyond the scope of this course! However, a useful collection of (loose) definitions for various "fairness types" can be found in [Google's What-If Tool documentation](https://pair-code.github.io/what-if-tool/ai-fairness.html).

## References

Cowgill, B., Dell'Acqua, F., Deng, S., Hsu, D., Verma, N., & Chaintreau, A. (2020, July). Biased programmers? or biased data? a field experiment in operationalizing ai ethics. In Proceedings of the 21st ACM Conference on Economics and Computation (pp. 679-681).

Mayson, S. G. (2018). Bias in, bias out. YAle lJ, 128, 2218.

Yudell, M., Roberts, D., DeSalle, R., Tishkoff, S., & 70 signatories. (2020). NIH must confront the use of race in science. Science, 369(6509), 1313-1314.

