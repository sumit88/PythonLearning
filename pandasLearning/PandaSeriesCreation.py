import pandas as pd
import numpy as np
import ProjectUitlities.Utils as Utils

Utils.printSpaces("Creating series from arrays")
data = np.array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
ser = pd.Series(data)
print(ser)

Utils.printSpaces("Creating series from lists")
list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
ser = pd.Series(list)
print(ser)

Utils.printSpaces("Accessing Element from Series with Position")
print(ser[:5])

Utils.printSpaces("Accessing Element Using Label(index)")
ser = pd.Series(data)
print(ser[3])
