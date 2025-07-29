import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

df = sns.load_dataset("tips")
count_df = df.groupby(['day', 'sex']).size().reset_index(name='count')
total_per_day = count_df.groupby('day')['count'].transform('sum')
count_df['percentage'] = (count_df['count'] / total_per_day) * 100

plt.figure(figsize=(8, 5))
sns.barplot(data=count_df, x='day', y='percentage', hue='sex', palette='Set2', edgecolor='black')

plt.title('نسبة الزبائن حسب الجنس خلال الأسبوع - seaborn')
plt.xlabel('Day')
plt.ylabel('Percentage %')
plt.legend(title='Sex')
plt.tight_layout()

# الامر المختلف هو حفظ الصورة بدل الإظهار
plt.savefig('seaborn_percentage_plot.png')
