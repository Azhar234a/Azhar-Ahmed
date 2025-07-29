import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

df = sns.load_dataset("tips")
grouped = df.groupby(['day', 'sex']).size().unstack()
percentages = grouped.div(grouped.sum(axis=1), axis=0) * 100

percentages.plot(kind='bar', figsize=(8, 5), edgecolor='black')
plt.title('نسبة الزبائن حسب الجنس خلال الأسبوع - matplotlib')
plt.xlabel('Day')
plt.ylabel('Percentage %')
plt.legend(title='Sex')
plt.tight_layout()

#الامر المختلف هو الأمر الجديد لحفظ الرسم
plt.savefig('matplotlib_percentage_plot.png')

# لم نستخدم plt.show() (مختلف عن التكليف)
