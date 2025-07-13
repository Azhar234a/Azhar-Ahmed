import numpy as np
I = np.eye(2, dtype='f'); I.dtype
dtype('float32')
low, high = np.lib.array_utils.byte_bounds(I)
high - low == I.size*I.itemsize
True
I = np.eye(2); I.dtype
dtype('float64')
low, high = np.lib.array_utils.byte_bounds(I)
high - low == I.size*I.itemsize
True