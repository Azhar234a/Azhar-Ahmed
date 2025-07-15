import pandas as pd

df = pd.DataFrame({
    "A": [1, 2, 2, 3],
    "B": ["x", "y", "y", "z"]
})

df.drop_duplicates(inplace=True)
print(df)
