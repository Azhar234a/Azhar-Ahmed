import numpy as np
import matplotlib.pyplot as plt

scores = np.array([65,72,80,55,90,45,85,70,75,60,95,50])
plt.boxplot(scores, vert=False)
plt.title("Distribution of student drades")
plt.xlabel("Grades")
plt.show()