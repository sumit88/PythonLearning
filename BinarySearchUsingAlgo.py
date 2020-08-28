c = 0


def bsearch(data, key):
    if not data:
        return None

    mid = int(len(data) / 2)
    if data[mid] == key:
        return 'found'
    elif data[mid] > key:
        return bsearch(data[:mid - 1], key)
    elif data[mid] < key:
        return bsearch(data[mid + 1:], key)


# for binary search the tree needs to be sorted

print(bsearch(range(100), 9))
print(bsearch(range(100), 50))

print(bsearch(range(100), 101))
print(bsearch(range(100), -1))
