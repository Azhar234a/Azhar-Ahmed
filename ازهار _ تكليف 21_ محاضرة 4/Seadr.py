#مخطط دائري
import seaborn as sns
import matplotlib.pyplot as plt

# تحميل البيانات
tips = sns.load_dataset("tips")

# حساب عدد الزبائن في كل يوم
day_count = tips['day'].value_counts()

# رسم Pie Chart
plt.figure(figsize=(8, 6))
plt.pie(day_count.values, labels=day_count.index, autopct='%1.1f%%', startangle=90)
plt.title('Pie Chart - Seaborn')
plt.show()


#مخطط نقاط مبعثرة
import seaborn as sns
import matplotlib.pyplot as plt

# تحميل البيانات
tips = sns.load_dataset("tips")

# رسم Scatter Plot
plt.figure(figsize=(8, 6))
sns.scatterplot(data=tips, x='total_bill', y='tip', hue='day')
plt.title('Scatter Plot - Seaborn')
plt.show()