#!/bin/python3

import math
import os
import re
import sys

if __name__ == '__main__':
    arr = []

    for _ in range(6):
        arr.append(list(map(int, input().rstrip().split())))

    data = []
    for i in range((len(arr[0])) - 2):
        for j in range(len(arr) - 2):
            temp = 0
            for k in range(3):
                temp += arr[i][j+k]
                temp += arr[i + 2][j + k]
            temp += arr[i + 1][j + 1]
            data.append(temp)

    print(max(data))