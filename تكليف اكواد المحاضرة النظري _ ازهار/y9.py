import pandas as pd

data = {
    "Name": ["Ali", "Sara", "Omar", "Lina", "Nour"],
    "Age": [23, 45, 31, None, 50]
}

df = pd.DataFrame(data)

# عالج القيم المفقودة بدون inplace لتجنب التحذير
df['Age'] = df['Age'].fillna(df['Age'].mean())

# تطبيق التطبيع
df['Age'] = (df['Age'] - df['Age'].min()) / (df['Age'].max() - df['Age'].min())

print(df)
