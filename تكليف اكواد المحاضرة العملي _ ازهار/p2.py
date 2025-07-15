import pandas as pd
d = {'col1': [1, 2, 3, 4, 7], 'col2': [4, 5, 6, 9, 5], 'col3': [7, 8, 12, 1, 11]}
df = pd.DataFrame(data=d)
print(df)
count_column = df.shape[1]
print("Number of columns:")
print(count_column)
count_row = df.shape[0]
print("Number of rows:")
print(count_row)