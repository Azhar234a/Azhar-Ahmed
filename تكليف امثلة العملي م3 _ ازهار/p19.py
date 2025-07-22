import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt


data = {

'Study_hours': [2, 3, 5, 7, 8, 10, 12, 15, 16, 18],

'Grades': [50, 55, 65, 70, 75, 80, 85, 90, 92, 95]
}
df = pd.DataFrame(data)
correlation = df['Study_hours'].corr(df['Grades'])
print(f"Correlation coefficient (Pearosn): {correlation:.2f}")
sns.regplot(x='Study_hours', y='Grades', data=df)
plt.title('Relationship between study hours and grades')
plt.show()

