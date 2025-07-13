import numpy as np
a = np.array([[1, 2], [3, 4]])
for index, x in np.ndenumerate(a):
 print(index, x)
(0, 0)
(0, 1)
(1, 0)
(1, 1)