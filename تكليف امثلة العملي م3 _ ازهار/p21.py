import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

np.random.seed(42)
data = {

'Age': np.random.randint(20, 60, 100),
'Income': np.random.randint (2000, 8000, 100),
'Savings': np.random.randint (100, 1000, 100)
}

data['Income'] = data['Age'] * 100 + np.random.normal(0, 500, 100)
data['Savings'] = 1000 - (data['Age'] * 10) + np.random.normal(0, 200, 100)
data['Savings'] = data['Savings'] + (data['Income'] * 0.005)

df = pd.DataFrame(data)
corr_matrix = df.corr()
print("Correlation matrix:")
print(corr_matrix)

sns.heatmap(corr_matrix, annot=True, cmap='coolwarm')
plt.title('Heat map of correlations between variables')
plt.show()

