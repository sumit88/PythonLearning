#!/bin/python3

import sys

n = int(input().strip())
a = list(map(int, input().strip().split(' ')))
# Write Your Code Here
count = 0
for i in range(len(a)):
    for j in range(i + 1, len(a)):
        if a[i] > a[j]:
            count += 1
            # temp = a[j]
            # a[j] = a[i]
            # a[i] = temp
            a[j], a[i] = a[i], a[j]  # much better way to swap two numbers

print(f'Array is sorted in {count} swaps.')
print(f'First Element: {a[0]}')
print(f'Last Element: {a[len(a) - 1]}')
