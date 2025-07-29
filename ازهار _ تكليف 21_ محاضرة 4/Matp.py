#مخطط دائري
import matplotlib.pyplot as plt
from seaborn import load_dataset

tips = load_dataset("tips")
day_counts = tips['day'].value_counts().sort_index()

plt.figure(figsize=(6, 6))
plt.pie(day_counts, labels=day_counts.index, autopct='%1.1f%%', startangle=90)
plt.title("Pie Chart - عدد الزبائن حسب اليوم")
plt.axis('equal')
plt.show()



#مخطط نقاط مبعثرة
import matplotlib.pyplot as plt
from seaborn import load_dataset
import numpy as np

tips = load_dataset("tips")
days = tips['day']
y_values = np.random.normal(loc=0, scale=0.1, size=len(days))  # قيم Y موزعة حول 0
plt.figure(figsize=(6, 4))
plt.scatter(days, y_values, color='purple', alpha=0.5)
plt.title("Scatter Plot - كل زبون كنقطة مبعثرة")
plt.xlabel("اليوم")
plt.ylabel("توزيع عشوائي")
plt.grid(True)
plt.show()

