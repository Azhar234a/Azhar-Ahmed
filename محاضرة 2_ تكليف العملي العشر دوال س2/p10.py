import pandas as pd

# 1) إنشاء بيانات تجريبية (أو استيرادها من ملف)
df = pd.DataFrame({
    'A': [1, 2, 3, 4, 5],
    'B': [10, 20, 30, 40, 50],
    'C': ['x', 'y', 'z', 'u', 'v']
})

# 2) اختيار عينة عشوائية من 3 صفوف مع تثبيت البذرة العشوائية لضمان تكرار النتيجة
sample_df = df.sample(n=3, random_state=42)

# 3) طباعة أو حفظ النتيجة
print(sample_df)
# مثلاً: sample_df.to_csv('sample_output.csv', index=False)
