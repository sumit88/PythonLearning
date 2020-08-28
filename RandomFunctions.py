import ProjectUitlities.Utils as Utils

Utils.printSpaces("Finding duplicate of 5")
d = [1, 2, 3, 4, 5, 6, 7, 7, 88, 9, 2, 32, 3, 4, 5, 1]
if len(list(filter(lambda x: x == 5, d))) > 1:
    print('there is a duplicate 5')
else:
    print('5 was not duplicated in the list')

Utils.printSpaces("Change things to upper case ")
d = ['sumit', 'chauhan']
print(list(map(lambda x: x.upper(), d)))
