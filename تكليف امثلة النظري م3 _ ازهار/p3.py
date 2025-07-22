import pandas as pd

df= pd.read_csv('sales_data.csv')
describe=df.describe()
print(describe)

mean_Sales=df['Sales'].mean()
print(f"The Mean of Sales is: {mean_Sales:4f}")
median_Sales=df['Sales'].median()
print(f"The Meadian of Sales is: {median_Sales:.4f}")

