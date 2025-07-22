import pandas as pd

# 1) إنشاء DataFrame (أو استيراده من ملف)
df = pd.DataFrame({
    'A': [1, 2, 3, 4, 5],
    'B': [10, 20, 30, 40, 50]
})

# 2) إضافة العمود E = 2 * A
df = df.assign(E=lambda x: x['A'] * 2)

# 3) طباعة النتيجة أو حفظها
print(df)
# أو مثلاً: df.to_csv('output.csv', index=False)
