import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

data={
    'Math':[80, 90, 70, 60],
    'Science': [85,75,65,95],
    'English': [70,80,90,60]
}
df=pd.DataFrame(data)
corr_matrix=df.corr()
sns.heatmap(corr_matrix, annot=True, cmap='coolwarm')
plt.title('Correlation of student grades across subjects')
plt.show()

