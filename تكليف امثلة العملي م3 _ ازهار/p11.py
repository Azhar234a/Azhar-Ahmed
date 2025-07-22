import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

data_skewed = np.random.exponential(scale=50000,size=1000)

sns.histplot(data_skewed, kde=True, color='red')
plt.title('Right_skewed distribution (individual income)')
plt.xlabel('Income ($)')
plt.ylabel('Frequency')
plt.show()
