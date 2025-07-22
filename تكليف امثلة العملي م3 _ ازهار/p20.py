import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

np.random.seed(42)
data = {

'Age': np.random.randint(20, 60, 100),
'Income': np.random.randint(2000, 8000, 100),
'Cost': np.random.randint(500, 3000, 100)
}

data['Income'] = data['Age'] * 100 + np.random.normal(0, 500, 100)
data['Cost'] = data['Income'] * 0.6 + np.random.normal(0, 300, 100)

df=pd.DataFrame(data)
corr_matrix = df.corr()
print("Correlation matrix:")
print(corr_matrix)

sns.heatmap(corr_matrix, annot=True, cmap='coolwarm')
plt.title('Heat map of correlations between variables')
plt.show()

