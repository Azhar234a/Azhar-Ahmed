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

plt.figure(figsize=(10, 6))
plt.hist(df['Sales'], bins=50, color='skyblue', edgecolor='black')
plt.title('توزيع المبيعات')
plt.xlabel('مقدار المبيعات')
plt.ylabel('عدد المعاملات')
plt.grid(True, alpha=0.3)
plt.savefig('sales_distribution.png')
plt.show()

plt.figure(figsize=(10, 6))
region_sales = df.groupby('Region')['Sales'].sum().sort_values(ascending=False)
region_sales.plot(kind='bar', color=['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728'])
plt.title('إجمالي المبيعات حسب المنطقة')
plt.xlabel('المنطقة')
plt.ylabel('إجمالي المبيعات')
plt.xticks(rotation=45)
plt.grid(True, alpha=0.3)
plt.savefig('sales_by_region.png')
plt.show()

plt.figure(figsize=(10, 6))
plt.scatter(df['Customer_Age'], df['Sales'], alpha=0.5, color='green')
plt.title('علاقة عمر العميل بالمبيعات')
plt.xlabel('عمر العميل')
plt.ylabel('مقدار المبيعات')
plt.grid(True, alpha=0.3)
plt.savefig('age_vs_sales.png')
plt.show()

plt.figure(figsize=(12, 8))
top_products = df['Product'].value_counts().nlargest(10).index
df_top_products = df[df['Product'].isin(top_products)]
sns.boxplot(x='Product', y='Sales', data=df_top_products)
plt.title('توزيع المبيعات لأهم 10 منتجات')
plt.xlabel('المنتج')
plt.ylabel('المبيعات')
plt.xticks(rotation=45)
plt.grid(True, alpha=0.3)
plt.savefig('sales_distribution_by_product.png')
plt.show()

# تحليل ANOVA لمعرفة ما إذا كانت هناك فروق ذات دلالة إحصائية في المبيعات بين المناطق
model = ols('Sales ~ C(Region)', data=df).fit()
anova_results = anova_lm(model)

print("\nنتائج تحليل ANOVA للمبيعات بين المناطق:")
print(anova_results)

# تفسير النتائج
alpha = 0.05
if anova_results['PR(>F)'][0] < alpha:
    print("\nهناك فرق ذو دلالة إحصائية في المبيعات بين المناطق (p-value = {:.4f})".format(anova_results['PR(>F)'][0]))
else:
    print("\nلا يوجد فرق ذو دلالة إحصائية في المبيعات بين المناطق (p-value = {:.4f})".format(anova_results['PR(>F)'][0]))

    # تحويل العمود Date إلى نوع datetime
    df['Date'] = pd.to_datetime(df['Date'])

    # حساب المبيعات اليومية
    daily_sales = df.groupby('Date')['Sales'].sum()

    plt.figure(figsize=(12, 6))
    daily_sales.plot(color='purple')
    plt.title('المبيعات اليومية عبر الزمن')
    plt.xlabel('التاريخ')
    plt.ylabel('إجمالي المبيعات اليومية')
    plt.grid(True, alpha=0.3)
    plt.savefig('daily_sales_trend.png')
    plt.show()