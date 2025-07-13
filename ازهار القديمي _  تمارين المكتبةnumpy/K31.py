import numpy as np
import warnings
x = np.array([0.0, 1.0, 2.0, 3.0, 4.0, 5.0])
y = np.array([0.0, 0.8, 0.9, 0.1, -0.8, -1.0])
z = np.polyfit(x, y, 3)
z
array([ 0.08703704, -0.81349206, 1.69312169, -0.03968254]) # may vary