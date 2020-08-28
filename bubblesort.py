def bubbleSort(data):
    for i in range(len(data)):
        for j in range(i, len(data)):
            if data[i] > data[j]:
                data[i], data[j] = data[j], data[i]

    return data


print(bubbleSort([1, 5, 3, 2, 2, 5, 7, 8, 9, 4, 2, 12, 1, 4, 5, 67, 8]))
