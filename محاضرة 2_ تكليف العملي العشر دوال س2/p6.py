import pandas as pd

# 1) إنشاء DataFrame بسيط
df = pd.DataFrame({
    'A': [1, 2, 3],
    'B': [10, 20, 30],
    'C': ['x', 'y', 'z']
})

# 2) تحويل العمود A إلى فهرس ثم تكديس الأعمدة B و C في مستوى صفّي واحد
stacked = df.set_index('A').stack()

print(stacked)
