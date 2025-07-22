import pandas as pd

# 1) إنشاء DataFrame
df = pd.DataFrame({
    'A': [1, 2, 3],
    'B': [10, 20, 30],
    'C': ['x', 'y', 'z']
})

# 2) تكديس البيانات
stacked = df.set_index('A').stack()

# 3) فكّ التكديس (unstack) لإعادة الأعمدة
unstacked = stacked.unstack()

print("البيانات بعد stack():")
print(stacked, "\n")

print("البيانات بعد unstack():")
print(unstacked)
