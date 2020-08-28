import collections
import ProjectUitlities.Utils as Utils

# The combined dictionary contains the key and value pairs in a specific sequence eliminating any duplicate keys.
# The best use of ChainMap is to search through multiple dictionaries at a time and
# get the proper key-value pair mapping.
dict1 = {'name': 'Sumit', 'lname': 'Chauhan'}
dict2 = {'name': 'Isha', 'lname': 'Khattar', 'age': 31}

combined = collections.ChainMap(dict1, dict2)  # order of it is important. First pair of keys are taken incase of
# duplicate values. this shows that chain map acts like a kind of a stack
print(combined)
# If there are duplicate keys, then only the value from the first key is preserved.
print('Keys = {}'.format(list(combined.keys())))
print('Values = {}'.format(list(combined.values())))

print(combined.get('name'))

Utils.printSpaces("updating chain maps")
print('just update the dictionary used to create the chained map and it will be done automatically')
dict1['gender'] = 'male'
print('Keys = {}'.format(list(combined.keys())))
print('Values = {}'.format(list(combined.values())))
