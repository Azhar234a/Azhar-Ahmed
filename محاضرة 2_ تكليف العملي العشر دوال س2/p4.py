import pandas as pd

# إنشاء DataFrame يحتوي على أعمدة A و B و C
df = pd.DataFrame({
    'A': [1, 2, 3],
    'B': [10, 20, 30],
    'C': ['x', 'y', 'z']
})

# استخدام melt لتحويل البيانات من شكل عريض إلى طويل
melted_df = pd.melt(df, id_vars=['A'], value_vars=['B', 'C'])

# طباعة النتيجة
print(melted_df)
