import pandas as pd

# 1) إنشاء DataFrame
df = pd.DataFrame({
    'A': [1, 2, 3],
    'B': [10, 20, 30]
})

# 2) تعريف دالة تستخدم مع pipe
def add_column(dataframe, name, values):
    dataframe[name] = values
    return dataframe

# 3) استخدام pipe لإضافة الأعمدة
result = (
    df.copy()
    .pipe(add_column, 'F', df['B'] + 100)
    .pipe(lambda d: d.assign(G=d['F'] / 10))
)

# 4) طباعة النتيجة
print(result)
