# importing pandas as pd
import pandas as pd

# importing numpy as np
import numpy as np
from ProjectUitlities import Utils

# dictionary of lists
dict = {'First Score': [100, 90, np.nan, 95],
        'Second Score': [30, 45, 56, np.nan],
        'Third Score': [np.nan, 40, 80, 98]}

# creating a dataframe from dictionary

df = pd.DataFrame(dict)

Utils.printSpaces("data cleaning ")

Utils.printSpaces("filling nulls")
# filling missing value using fillna()
# inplace is set to false which means data will not be changed in original dataframes
print(df.fillna(0, inplace=False))

Utils.printSpaces("dropping nulls")
# filling missing value using fillna()
# inplace is set to false which means data will not be changed in original dataframes
print(df.dropna())  # by default axis is 0 which means all the rows containing null will be dropped.

Utils.printSpaces("dropping columns nulls")
# filling missing value using fillna()
# inplace is set to false which means data will not be changed in original dataframes
print(df.dropna(axis=1))  # by default axis is 0 which means all the rows containing null will be dropped.
