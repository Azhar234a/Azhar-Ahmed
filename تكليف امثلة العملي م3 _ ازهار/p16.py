import seaborn as sns
import matplotlib.pyplot as plt

data={'Salary': [2000,2500,3000,3500,4000,4500,5000,10000,15000]}
sns.boxplot(data=data, y='Salary')
plt.title('Distribution of salaries (wit outliers)')
plt.show()