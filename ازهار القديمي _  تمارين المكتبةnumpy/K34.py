import numpy as np
x = np.ma.array([1, 2, 3, 4], mask=[0, 1, 0, 1])
np.ma.setdiff1d(x, [1, 2])
masked_array(data=[3],
mask=[False, True],
fill_value=999999)