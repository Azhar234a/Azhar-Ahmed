import numpy as np
x=np.array([1,2,3,4])
x=np.array([2,4,5,4])
coefficients=np.polyfit(x,y,1)
print("coefficients(Slope,Intercept):" , coefficients)