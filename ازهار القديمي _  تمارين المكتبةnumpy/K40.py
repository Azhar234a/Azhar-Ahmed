import numpy as np
x = np.arange(10)
y = x + 1
it = np.nditer([x, y])
next(it)
(array(0), array(1))
it2 = it.copy()
next(it2)
(array(1), array(2))