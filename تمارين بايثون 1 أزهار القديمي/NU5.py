point1=[1,2,3]
point2=[4,5,6]
distance = sum([(i-j)**2 for i,j in zip(point1,point2)])**0.5
print("distance:", distance)
import numpy as np
distance = np.linalg.norm(np.array(point1) - np.array(point2))
print("distance:" , distance)
