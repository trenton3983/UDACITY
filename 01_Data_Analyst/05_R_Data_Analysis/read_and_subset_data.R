#test_dir <- 'E:/Users/Trenton J. McKinney/PycharmProjects/UDACITY/01_Data_Analyst/05_R_Data_Analysis'
test_dir <- 'C:/PythonProjects/UDACITY/01_Data_Analyst/05_R_Data_Analysis'
setwd(test_dir)
statesInfo <- read.csv('stateData.csv')

stateSubset <- subset(statesInfo, state.region == 1) # returns a subset where region = 1
head(stateSubset, 2)
dim(stateSubset)

stateSubsetBracket <- statesInfo[statesInfo$state.region == 1, ] # also returns subset, blank after (,) is all columns
head(stateSubsetBracket, 2)
dim(stateSubsetBracket)


cat("\014") # clear console

subset(statesInfo, illiteracy <= 0.5 & highSchoolGrad >= 50.0 )
