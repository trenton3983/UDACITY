import numpy as np
import pandas as pd

file_path = 'E:/Users/Trenton J. McKinney/Documents/UDACITY/02 Data Analysis/Lesson 2 - NumPy & Pandas for 1D Data/Downloadables/'
i = pd.read_csv(file_path + 'employment_above_15.csv')

print i['Country'].unique()
