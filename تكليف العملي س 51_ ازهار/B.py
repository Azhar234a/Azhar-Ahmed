import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from scipy import stats
from statsmodels.formula.api import ols
from statsmodels.stats.anova import anova_lm
from datetime import datetime


df = pd.read_csv('sales_data.csv')
print("معلومات عن البيانات:")
print(df.info())
print("\nإحصائيات وصفية للبيانات:")
print(df.describe())
print("\nعرض أول 5 صفوف من البيانات:")
print(df.head())
print("\nعدد القيم المفقودة في كل عمود:")
print(df.isnull().sum())
df['Sales'] = df.groupby('Product')['Sales'].transform(lambda x: x.fillna(x.mean()))

# إذا بقي أي قيم مفقودة (للمنتجات التي لا تحتوي على أي مبيعات مسجلة)، نملؤها بالصفر
df['Sales'] = df['Sales'].fillna(0)

# ملء القيم المفقودة في عمود المنتج بالقيمة "Unknown"
df['Product'] = df['Product'].fillna('Unknown')

# ملء القيم المفقودة في عمود المنطقة بالقيمة الأكثر تكراراً
most_common_region = df['Region'].mode()[0]
df['Region'] = df['Region'].fillna(most_common_region)

# ملء القيم المفقودة في عمود عمر العميل بالمتوسط
df['Customer_Age'] = df['Customer_Age'].fillna(df['Customer_Age'].mean())

# التحقق من عدم وجود قيم مفقودة بعد المعالجة
print("\nعدد القيم المفقودة بعد المعالجة:")
print(df.isnull().sum())