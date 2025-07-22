import pandas as pd

# 1) إنشاء بيانات تجريبية
df = pd.DataFrame({
    'A': [1, 2, 3, 4, 5, 6],
    'B': [10, 20, 30, 40, 50, 60]
})

# 2) حساب المتوسط المتحرك (Rolling Mean) بنافذة طولها 3 صفوف
rolling_mean = df[['A', 'B']].rolling(window=3).mean()

print("القيم الأصلية:")
print(df, "\n")

print("المتوسط المتحرك (window=3):")
print(rolling_mean)
