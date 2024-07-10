# Project 1: Load and clean financial data.
# Deadline: 1 week
# Mandatory: Use pandas to read CSV files and handle missing values.

#imports
import pandas as pd
import numpy as np

# Dictionary of lists
dict = {'First Score':[100,90,np.nan,95],
        'Second Score':[30,45,56,np.nan],
        'Third Score':[np.nan,40,80,98]}

# creating a dataframe from list
df = pd.DataFrame(dict)

# using isnull() function
df.isnull

