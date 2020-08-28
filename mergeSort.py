def merge_sort(values):
    if len(values) > 1:
        m = len(values) // 2
        leftconquer = values[:m]
        rightConquer = values[m:]
        left = merge_sort(leftconquer)
        right = merge_sort(rightConquer)

        values = []

        while len(left) > 0 and len(right) > 0:
            if left[0] < right[0]:
                values.append(left[0])
                left.pop(0)
            else:
                values.append(right[0])
                right.pop(0)

        for i in left:
            values.append(i)
        for i in right:
            values.append(i)

    return values


print(merge_sort([1, 4, 2, 5, 2, 32, 5, 62, 1, 4, 6, 7, 234, 1, 12, 5, 6, 3, 1, 1]))
