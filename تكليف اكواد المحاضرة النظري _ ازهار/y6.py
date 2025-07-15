import pandas as pd

data = {
    "age": [25, 30, None, 22, 28],      # None تمثل قيمة مفقودة
    "score": [85, None, 78, 90, None]
}

df = pd.DataFrame(data)    # أنشئ DataFrame من القاموس
df.fillna(df.mean(numeric_only=True), inplace=True)  # املأ القيم الفارغة بالمتوسط
print(df)
