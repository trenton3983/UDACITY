reddit <- 'C:/PythonProjects/UDACITY/01_Data_Analyst/05_R_Data_Analysis/'
setwd(reddit)
reddit_data = read.csv('C:/PythonProjects/UDACITY/01_Data_Analyst/05_R_Data_Analysis/eda-course-materials/lesson2/reddit.csv')
str(reddit_data)
head(reddit_data, 10)
View(reddit_data)
table(reddit_data$employment.status)
