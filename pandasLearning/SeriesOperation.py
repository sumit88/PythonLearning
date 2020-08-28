# add() 	Method is used to add series or list like objects with same length to the caller series
# sub() 	Method is used to subtract series or list like objects with same length from the caller series
# mul() 	Method is used to multiply series or list like objects with same length with the caller series
# div() 	Method is used to divide series or list like objects with same length by the caller series
# sum() 	Returns the sum of the values for the requested axis
# prod() 	Returns the product of the values for the requested axis
# mean() 	Returns the mean of the values for the requested axis
# pow() 	Method is used to put each element of passed series as exponential power of caller series and returned the results
# abs() 	Method is used to get the absolute numeric value of each element in Series/DataFrame
# cov() 	Method is used to find covariance of two series

import numpy as np
import pandas as pd
import ProjectUitlities.Utils as Utils
import matplotlib.pyplot as plt

data = np.array([1, 2, 1, 4, 5])

ser = pd.Series(data=data)

print(ser.add(1))
print(ser.mul(2))
print(ser.mul([1, 2, 3, 4, 5]))

Utils.printSpaces("selecting top 2 rows")
print(ser.head(2))
ser.plot()
# sudo apt-get install python-tk
# sudo apt-get install python3-tk
# plt.show()

Utils.printSpaces("map function can take lambdas")
squared = ser.map(lambda x: x ** 2)
print(squared)

Utils.printSpaces("to filter the value based on data")
print(squared[squared > 10])

Utils.printSpaces("filter()  method works on index and not data")
names = ["Sumit", "Chauhan", "Male", 31]
nameSer = pd.Series(data=names)
nameSer.index = ["fname", "lname", "gender", "age"]
filteredNames = nameSer.filter(like="name")
print(filteredNames.to_dict())

Utils.printSpaces("converting series to dataframes")
filteredNamesDf = filteredNames.to_frame()
filteredNamesDf.columns = ["original"]
print(filteredNamesDf.dtypes)
namesWithTitles = filteredNamesDf["original"].map(lambda x: 'Mr ' + x)
print(pd.concat([filteredNames, namesWithTitles]))

Utils.printSpaces("adding columns")
print(filteredNamesDf.head(2))
filteredNamesDf['with_tiltes_2'] = filteredNamesDf.apply(lambda x: "MR " + x["original"], axis=1)
print("Sonal")
print(filteredNamesDf.head(2))
newdfs = filteredNamesDf.assign(with_tiltes_3=lambda x: "Miss " + filteredNamesDf["original"])
print("Sonal2")
print(newdfs.head(2))

df2 = pd.concat([filteredNames, namesWithTitles], axis=1)
df2.columns = ["name", "with_titles"]
print(df2)

print(df2.rename(columns={"with_titles": "titles"}))

print(df2.rename(index={"fname": "first_name"}))

Utils.printSpaces("Change column names to upper case")
df2.columns = map(str.upper, df2.columns)
print(df2)
