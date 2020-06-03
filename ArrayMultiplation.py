arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

l = lambda x: print(x)

evenList = list(filter(lambda x: x % 2 == 0, arr))

print(evenList)

squaredList = list(map(lambda x: x ** 2, arr))

print(squaredList)

print(list(zip(arr, squaredList)))

print(dict(list(zip(arr, squaredList))))  # convert tuple to dictionary

print(list(map(lambda x: (x, x * 2), arr)))

arr2 = [11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
arr.extend(arr2)
print(arr)
