import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df = sns.load_dataset('titanic')

plt.figure(figsize=(8, 5))
sns.boxplot(x='survived', y='age', data=df)
plt.xticks([0, 1], ['لم ينجُ', 'نجا'])
plt.title('مقارنة أعمار الناجين والضحايا')
plt.xlabel('النجاة')
plt.ylabel('العمر')
plt.grid(True)
plt.show()

pivot_table = pd.pivot_table(df, values='survived', index='sex', columns='pclass', aggfunc='mean')

print("معدل البقاء حسب الجنس والطبقة:")
print(pivot_table.round(2))  # تقريبه لعددين عشريين

pivot_table.plot(kind='bar', figsize=(8,5))
plt.title('معدل البقاء حسب الجنس والطبقة')
plt.ylabel('معدل البقاء')
plt.xlabel('الجنس')
plt.xticks(rotation=0)
plt.legend(title='الطبقة')
plt.grid(True)
plt.show()
