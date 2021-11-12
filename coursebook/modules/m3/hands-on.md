# Module 3: hands-on session

## Description
In this hands-on session participants are divided in groups of 4 o 5 participants and paired with a helper. Each group, 
should choose one of the proposed tasks (or propose a new one if keen!) and work together on it. At the end of the
session the students will present their work to the class.
The timeline for this session is the following:
- Phase 1: Presentation of tasks and goals of the hands-on session (15 minutes),
- Phase 2: Groups are formed and students choose task to develop (15 minutes)  
- Phase 3: Work on the tasks (2.5 hours + with two 15 m break) 
- Phase 4: Students presenting their findings and discussion (1 hour)      

Students are encouraged to use code developed in the hands-on session for module 2 and/or the data exploration notebook in
_Section 3.5_. They can use data from the UK or choose another country. Presentations should last between 5 and 10 minutes.

## Proposed tasks      

1. **Use data visualisation to further explore relationship between variables**: In _Section 3.5_ we did a initial exploration of the relationship between variables 
   focusing particularly on deprivation index and accommodation and self-reported health. Since our research question, and the
   modeling tasks that we will develop in Module 4 it is imperative to further understand the relationship between these and other psychosocial variables
   with the self-reported health and each other. For example:    
   - Education variables (`ISCED` or `Education`)
   - Mental well-being variables (`MentalWellbeingIndex`)
   - Any other psychosocial you find interesting.
     
    Think of ways of visualising these relationships that would  convince a PI (and yourself!) and a given variable should be part of the model.


2. **Use data visualisation to explore data missingness**: In _Section 3.5_ we looked at the missingness of some variables superficially, and for simplicity
   we decided to drop rows with missing values. This is a dangerous approach, particularly if we have data that is not missing completely at random. For example, 
   if for some unknown factor people living in the most deprived areas are less likely to answer to some survey question 
   that group would end up being underrepresented in our dataset. In this task you are invited to :
   - Further explore the missingness in our variables of interest related to Module 4 (`AgeCategory`,`DeprIndex`,`ISCED`,
     `Children`,`MentalWellbeingIndex`,`AccomProblems`,`SRH`) and advice if it was a sensible approach to drop the rows as done in _Section 3.5_.
    - Explore other methods of dealing with missing data, such as imputation or prediction of the missing values (some of these are mentioned in Module 2).
    

3. **Be a data journalist for a day**: After doing some exploration on the dataset use data visualisation to tell a story 
   from the data. You are free to decide which story you want to tell!