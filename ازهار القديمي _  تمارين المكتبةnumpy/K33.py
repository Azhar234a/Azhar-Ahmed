import numpy as np
x = np.ma.array([1, 3, 3, 3], mask=[0, 0, 0, 1])
y = np.ma.array([3, 1, 1, 1], mask=[0, 0, 0, 1])
np.ma.intersect1d(x, y)
masked_array(data=[1, 3],
mask=[False, False, True],
fill_value=999999)