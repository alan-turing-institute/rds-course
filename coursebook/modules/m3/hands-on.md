# Module 3 hands-on session

## Description
In this hands-on session participants are divided in groups of 4 to 5 participants and paired with a helper. Each group, 
should choose one of the proposed tasks (or propose a new one if keen!) and work together on it. At the end of the
session the students will present their work to the class.
The timeline for this session is the following:
- Phase 1: Presentation of tasks and goals of the hands-on session (15 minutes),
- Phase 2: Groups are formed and students choose task to develop (15 minutes)  
- Phase 3: Work on the tasks (2.5 hours + with two 15 m breaks) 
- Phase 4: Students present their findings and discussion (1 hour)      

Students are encouraged to use code developed in the hands-on session for module 2 and/or the data exploration notebook in [_Section 3.5_](section3.5). They can use data from the UK or choose another country. Presentations should last between 5 and 10 minutes.

## Proposed tasks      

1. **Use data visualisation to further explore relationship between variables**: In [_Section 3.5_](section3.5) began exploring the relationships between some of the variables, focusing particularly on deprivation index and accommodation and self-reported health. Our research questions requires examining variables beyond these two, and in Module 4 we will be using more variables. It is important to further understand the relationships between our chosen variables.
   with the self-reported health and each other. For example:    
   - Other material variables (e.g. `Household Size`, or `Children`)
   - Education variables (`ISCED` or `Y11_Education`)
   - Mental well-being variables (`MentalWellbeingIndex`)
   - Any other psychosocial you find interesting.
     
    Think of ways of visualising these relationships that would  convince a PI (and yourself!) and a given variable should (or should not) be part of the model.

```{note}
In Module 4's hands-on you will be building your own models with variables of your choosing. We have selected a subset of variables to make the task manageable, but feel free to explore further and assess any variables in the EQLS dataset that you think are interesting. You will be able to use these variables in Module 4's hands-on.
```
2. **Use data visualisation to explore data missingness**: In [_Section 3.5_](section3.5) we looked at the missingness of some variables rather superficially. For simplicity we decided to drop rows with missing values. This is a dangerous approach, particularly if we have data that is not missing completely at random. For example, if for some unknown factor people living in the most deprived areas are less likely to answer to some survey question that group would end up being underrepresented in our dataset. In this task you are invited to:
   - Further explore the missingness in our variables of interest related to Module 4 (`AgeCategory`,`DeprIndex`,`ISCED`,
     `Children`,`MentalWellbeingIndex`,`AccomProblems`,`SRH`) and advise if it was a sensible approach to drop the rows as done in [_Section 3.5_](section3.5).
    - Explore other methods of dealing with missing data, such as imputation or prediction of the missing values (some of these are mentioned in Module 2).


3. **Be a data journalist for a day**: After doing some exploration on the dataset use data visualisation to tell a story from the data. You are free to decide which story you want to tell!
 
