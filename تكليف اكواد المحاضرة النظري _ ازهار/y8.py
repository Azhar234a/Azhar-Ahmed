import pandas as pd

# إنشاء بيانات تجريبية
data = {
    "Name": ["Ali", "Sara", "Omar", "Lina"],
    "Gender": ["male", "female", "Male", "Female"]
}

df = pd.DataFrame(data)

df['Gender'] = df['Gender'].str.capitalize().map({'Male': 1, 'Female': 0}).fillna(-1)

print(df)
