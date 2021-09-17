# Legality and Ethics

## Legality

**Big disclaimer: we are not legal experts and this is not legal advice. The content in this section is aimed at making you aware of these issues. If in any doubt, speak to an expert.**

We need to consider who **owns** the data that we wish to use and what **restrictions** they or regulatory/governing bodies may have put in place.

### Licences

> A licence agreement is a legal arrangement between the creator/depositor of the data set and the data repository, signifying what a user is allowed to do with the data. 
*The Data Management Expert Guide by CESSDA ERI*

As a user, it is your responsibility to abide by the terms of a licence when making use of a dataset. This is similar to licensing for software.

Licences range in the freedoms they give to users. Licences that grant users freedoms over (re)use and (re)distribution are *permissive*. Some common examples are:

 - [Creative Commons Attribution 4.0 International (CC BY 4.0)](https://creativecommons.org/licenses/by/4.0/)
     - the dataset may be shared and adapted as long as credit is given, the original is linked, and any changes are noted.
 - [CDLA-Sharing-1.0](https://cdla.io/sharing-1-0/)
     - a "copy-left" license. Similar restrictions to CC BY 4.0 but you must use the same license if resharing the data (or "enhanced data"). Importantly, restrictions **do not** apply to results of computational use.  


However, not all licences give so many freedoms. It's always worth checking.

NB: GitHub's default stance for [no licence](https://choosealicense.com/no-permission) is that the work is under exclusive copyright by default.

More information on data licences can be found in [The Turing Way](https://the-turing-way.netlify.app/reproducible-research/licensing/licensing-data.html).


### Data Protection & GDPR


From https://www.gov.uk/data-protection:
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


#### What's personal data?

Personal data is information about a particular living individual. It doesn't need to be "private" information.

Truly anonymous information isn't covered - but if you could use the data to identify someone (e.g. by combining it with another source) it still counts as personal data.

Summarised from: https://ico.org.uk/for-organisations/guide-to-data-protection/introduction-to-data-protection/some-basic-concepts/

See more at: https://ico.org.uk/for-organisations/guide-to-data-protection/guide-to-the-general-data-protection-regulation-gdpr/key-definitions/what-is-personal-data/

#### Does it apply to me?

> The law applies to any ‘processing of personal data’, and will catch most businesses and organisations, whatever their size.
*ICO Guide to Data Protection*

However, there are a few exemptions to GDPR and some things that are simply outside it's scope.

Personal or household activities are considered outside of the scope of the UK's GDPR. Data **only** for personal use won't make  you subject to GDPR.

Crucially, for academia and research, there are some exemptions. The details of these can be complicated and are certainly beyond the scope of this course. Each organisation will have their own stance on GDPR and you should consult internally to determine how to proceed.


For exemptions, see: https://ico.org.uk/for-organisations/guide-to-data-protection/guide-to-the-general-data-protection-regulation-gdpr/exemptions/


### Commercial agreements

Research projects are often collaborative efforts that may span multiple organisations. Commonly, these collaborations take place under some defined commercial agreement (a contract). Such an agreement may impact on your use of data.

For example:

*VacuumOrg have a contract with your organisation, DullResearchInc, to conduct research into consumer spending on robot vacuum cleaners. As part of this research, MarketingOrg have shared some survey data with you that they have collected over the last 6 months. The data collection was expensive and the data is considered hot-property by MarketingOrg; they don't wish their competitors to have access to it and only share it with you under a Non-Disclosure Agreement (NDA).*

*You want to transfer the data (5Mb) from your colleagues PC to your work laptop. Assuming some oddly limited options, which of the following do you do?*
*A) upload it to your public GitHub repository so you can pull it down later*
*B) transfer via a DullResearchInc USB stick*


## Ethics

**Ethics are a shared responsibility, however, it's another area that we should all feel comfortable seeking expert advice. At Turing, we have an Ethics Advisory Board that we can look to for guidance.**


Although there will be a lot of crossover between legailty and ethics, we should be aware that there may be additional ethical considerations over use of a dataset, even when its use is deemed legal.


For example:

*The UK data service lists the European Quality of Life Time Series, 2007 and 2011: Open Access dataset available for download and use under a CC BY 4.0 licence. We run through an internal data protection review and are confident that, legally, we can proceed under TODO provision.*

*However, we may wish to consider the consent under which this data was originally gathered. Did the respondees to this survey explicitly consent to its secondary use in research (or teaching, in this case)? If not, can we assme implied consent? Do we need consent at all, in this case? TODO: draw from any ethics review.*


### Bias in, bias out

We should also consider *how* and *why* the data was collected. Is it suitable for use in our project? Would use of this data lead us to a "bias in, bias out" situation with any resulting model?

TODO: example