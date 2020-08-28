import pandas as pd
import ProjectUitlities.Utils as Utils

# dictionary of lists
dict = {'name': ["aparna", "pankaj", "sudhir", "Geeku"],
        'degree': ["MBA", "BCA", "M.Tech", "MBA"],
        'score': [90, 40, 80, 98]}

# creating a dataframe from a dictionary
df = pd.DataFrame(dict)

# iterating over rows using iterrows() function
Utils.printSpaces("data frame iterationss using iterrows")
for i, j in df.iterrows():
    print(f'dataframa indes {i} with data: \n {j} \n')
    print()

Utils.printSpaces("Iterating Columns ")
columns = list(df)
print(df)
print(f'columns are  {columns}')
for i in columns:
    # printing the third element of the column
    print(df[i][2])

Utils.printSpaces("printing second row ")
print(df.iloc[1])

Utils.printSpaces("fetching second Columns ")
print(df[df.columns[2]])

Utils.printSpaces("fetching second Columns using slice ")
print(df)
print(df.iloc[:, 1])



