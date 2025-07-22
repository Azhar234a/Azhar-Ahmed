import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import f_oneway

df = pd.read_csv('train.csv')
print(df.head())

print(df.info())
print(df.describe())
print(df.isnull().sum())

df['age'] = df['age'].fillna(df['age'].median())
df['embark_town'] = df['embark_town'].fillna(df['embark_town'].mode()[0])

df.drop(columns=['deck', 'class', 'alone'], inplace=True, errors='ignore')  # deck ليس ضروريًا، واستخدم errors='ignore' للأمان

print("المتوسط:\n", df.mean(numeric_only=True))
print("الوسيط:\n", df.median(numeric_only=True))
print("المنوال:\n", df.mode(numeric_only=True).iloc[0])

print("الانحراف المعياري:\n", df.std(numeric_only=True))
print("التباين:\n", df.var(numeric_only=True))
print("معامل الانحراف:\n", df.skew(numeric_only=True))

plt.figure(figsize=(6,4))
sns.boxplot(x='survived', y='age', data=df)
plt.xticks([0, 1], ['مات', 'نجا'])
plt.title("Box Plot: العمر والنجاة")
plt.show()

pivot = pd.pivot_table(df, values='survived', index='sex', columns='n_siblings_spouses', aggfunc='mean')
print(pivot.round(2))

pivot.plot(kind='bar', figsize=(7,5))
plt.title("معدل البقاء حسب الجنس وعدد المرافقين")
plt.ylabel("نسبة البقاء")
plt.xlabel("الجنس")
plt.legend(title='مرافقين')
plt.grid(True)
plt.show()

corr = df.corr(numeric_only=True)
sns.heatmap(corr, annot=True, cmap="YlGnBu")
plt.title("خريطة الارتباط")
plt.show()

group1 = df[df['survived'] == 0]['age']
group2 = df[df['survived'] == 1]['age']
f_stat, p_val = f_oneway(group1, group2)
print(f"ANOVA p-value = {p_val:.4f}")
