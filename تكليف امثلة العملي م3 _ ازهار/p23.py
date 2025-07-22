import pandas as pd

df = pd.read_csv('sales_data.csv')
from scipy.stats import f_oneway
df= df.dropna(subset=['Sales', 'Product'])
laptop = df[df['Product'] == 'Laptop']['Sales']
mouse = df[df['Product'] == 'Mouse']['Sales']
keyboard = df[df['Product'] == 'Keyboard']['Sales']

f_statistic, p_value = f_oneway(laptop, mouse, keyboard)
print(f"The F-statistic is: {f_statistic:.2f}")
print(f"The P-value is: {p_value:.2f}")

