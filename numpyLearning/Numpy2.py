import numpy as np

rg = np.random.default_rng(1)

def f(x, y):
    return 10 * x + y


z = np.fromfunction(f, (5, 4), dtype=int)
#print(z)

z = np.r_[23: 29, 0, 4]
#print(z)

a = np.floor(10 * rg.random((2, 12)))
print(a)

b = np.split(a,2)
#print(b)

b = np.hsplit(a,(3,4))
print(b)

b = np.hsplit(a,(3,5))
print(b)



####################################

arr1 = np.ones((3,3))
print(arr1)

arr2 = arr1
arr2[0] =0
print(arr2)
print(arr1)  # value of a1 also changes cause it numpy usses the the reference to object while assignment in arr2 = arr1

