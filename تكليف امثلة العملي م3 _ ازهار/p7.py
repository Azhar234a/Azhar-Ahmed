import matplotlib.pyplot as plt
import numpy as np

data = np.random.normal(100, 15, 200)

plt.hist(data, bins=10, color='skyblue', edgecolor='black')
plt.title("Distribution with Matplotlib")
plt.xlabel("Value")
plt.ylabel("Frequency")
plt.show()
