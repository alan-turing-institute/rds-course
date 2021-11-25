
# Module 4 hands-on session

## Description
In this hands-on session participants are divided in groups of 4 or 5 participants and paired with a helper. Each group should choose one of the proposed tasks (or propose a new one if keen!) and work together on it. At the end of the session the students will present their work to the class.

The timeline for this session is the following:

- Phase 1: Presentation of tasks and goals of the hands-on session (15 minutes)
- Phase 2: Groups are formed and students choose task to develop (15 minutes)
- Phase 3: Work on the tasks (2.5 hours + with two 15 m break)
- Phase 4: Group discussion of findings (30 minutes)
- Phase 5: Course wrap-up (30 minutes)

Students are encouraged to use code developed in the hands-on session for module 3 and/or the data exploration notebook in Sections 4.3 and 4.4. 
They can use data from the UK or choose another country. This is your chance to draw mathematical conclusions from the dataset.

## Proposed tasks

1. **Improving the models**: We invite you to try to improve/modify the models discussed in _Section 4.4_. Some suggestions: 
        
    - Adding new variables and/or [interactions variables](https://en.wikipedia.org/wiki/Interaction_(statistics))  to the model. Does this new model improve your knowledge?
    
    - The dataset is very imbalanced (the majority is 'good health'). We have addressed this in sections 4.3/4.4 by changing the threshold of our p(x) classifier. But there are other ways of dealing with an imbalanced dataset (for some ideas see [here](https://towardsdatascience.com/how-to-deal-with-imbalanced-data-34ab7db9b100)). Investigate how some of these change your modelled conclusions.
    
2. **Prediction & Simulation**.

    - Logistic regression predicts the mean of a bernouilli distribution. Essentially, you get a generative model for each combination of predictor variable values. Have a play with simulating data from this bernouilli distribution to generate a new dataset of N people (we do this a bit in 4.1 and 4.3). Does our simulated dataset look anything like our real dataset? 
        - Can you visualise how p(x) changes when you change specific variables while keeping the others constant? 

    - In the above point we have assumed a single point estimate of p(x). But there is uncertainty in our coefficients, and therefore uncertainty in our p(x). What if we sample from this uncertainty when generating p(x)? 

3. **Comparative analysis with another country**: Up to now we have only looked at the UK, but what happens in other countries?
How good is the performance if you use a model trained with UK data in another country? How different is the model (coefficients, performance, etc) trained with data from
   another country (e.g Poland vs the model of the UK shown in _Section 4.4_). Can you conclude that the same factors have different
   impact between the countries? Feel free to compare between any country you'd like.
   
    
We expect you to compare and discuss in detail what you have learned from these new models and think what would be the answer
to the research question. 
   
4. **Imputation**: In module 3 we explored missingness in the data, and touched on different ways of dealing with this. Here we could explore the effect of different methods of imputation. For any method of imputation, the critical thing is to compare model output on the imputed data with the model output on the uninmputated data to assess how it changes the conclusions. Some suggestions of increasing complexity:

 -  Replacing missing rows with the average of the missing variables. 

 -  Sample from a variable's distribution to fill out the missing rows. You could:
    - sample with replacement from the empirical values
    - create a probability estimate of the distribution (e.g. kde) and sample from that.
    - something else...

- Model the missing variable as dependent on present variables. You could apply our generalised regression framework: pick potential predictors, select your distribution for the residuals, see if you want a link function other than the identity function.
    

## Final discussion session

Group discussion with the following points. We don't have "right answers" for this discussion. 

1. If the research question asks for an overall assessment of all Europe. How do we appropriately combine the models?
   
2. Is there a better way of modeling dataset given the research question?
   
3. After everything you've done in all the hands on sessions, what would be your answer to
the research question? What else has to be done? 

