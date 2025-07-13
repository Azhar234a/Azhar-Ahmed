import numpy as np
x = np.eye(3)
x.getfield(np.float64)
array([[1., 0., 0.],
[0., 1., 0.],
[0., 0., 1.]])
x.setfield(3, np.int32)
x.getfield(np.int32)
array([[3, 3, 3],
[3, 3, 3],
[3, 3, 3]], dtype=int32)
x
array([[1.0e+000, 1.5e-323, 1.5e-323],
[1.5e-323, 1.0e+000, 1.5e-323],
[1.5e-323, 1.5e-323, 1.0e+000]])
x.setfield(np.eye(3), np.int32)
x
array([[1., 0., 0.],
[0., 1., 0.],
[0., 0., 1.]])

