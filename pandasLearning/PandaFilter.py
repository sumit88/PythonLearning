import numpy as np
import pandas as pd
import ProjectUitlities.Utils as Utils

data = {"fname": ["Sumit", "Isha"], "lname": ["Chauhan", "Khattar"], "Age": [31, 31]}

df1 = pd.DataFrame(data)

Utils.printSpaces("Original dataframe")
print(df1)

Utils.printSpaces("filter where name is Sumit \n rows not matching the columns will be converted to null")

print(df1.where(df1["fname"] == "Sumit").dropna())

Utils.printSpaces("using queries , age >30 ")
print(df1.query("Age > 30"))

Utils.printSpaces("using queries , fname is Sumit ")
print(df1.query("fname == 'Sumit' "))
