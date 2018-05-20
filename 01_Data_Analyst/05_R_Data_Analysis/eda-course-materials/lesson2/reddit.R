
directory <- 'E:/Users/Trenton J. McKinney/PycharmProjects/UDACITY/01_Data_Analyst/05_R_Data_Analysis/eda-course-materials/lesson2'
setwd(directory)

reddit<- read.csv('reddit.csv')

table(reddit$employment.status)
summary(reddit) 

str(reddit)

levels(reddit$age.range)
levels(reddit$income.range)

qplot(data = reddit, x = age.range)
qplot(data = reddit, x = income.range)


# Setting Levels of Ordered Factors Solution
reddit$age.range <- ordered(reddit$age.range, levels = c("Under 18", "18-24", "25-34", "35-44", "45-54", "55-64",
                                                         "65 or Above"))
reddit$income.range <- ordered(reddit$income.range, levels = c("Under $20,000", "$20,000 - $29,999", "$30,000 - $39,999",
                                                               "$40,000 - $49,999", "$50,000 - $69,999", "$70,000 - $99,999",
                                                               "$100,000 - $149,999", "$150,000 or more"))


# Alternate Solution
reddit$age.range <- factor(reddit$age.range, levels = c("Under 18", "18-24", "25-34", "35-44", "45-54", "55-64",
                                                        "65 or Above"), ordered = T)