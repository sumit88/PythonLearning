import numpy as np
from numpy import newaxis

rg = np.random.default_rng(1)

a = np.array([[1, 1],
              [2, 2]], dtype=np.uint8)
print(a.ndim)

b = np.array([[11, 11],
              [22, 22]], dtype=np.uint8)

print(a[:1])

print('============================')

c = np.column_stack((a[:, None], b[:, None]))
print(c)

print('============================')

c = np.column_stack((a, b))
print(c)

print('============================')

c = np.hstack((a, b))
print(c)
print('============================')

print(c[:1])

d = np.tile(8,(6,5 ,9))

print(d[0,:,:])


