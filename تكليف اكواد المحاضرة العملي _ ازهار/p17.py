sales=pd.read+csv('sales_data.csv')
print(sales.head(3))
high_sales=sales[sales['Revenue'] > 100]
product_sales=sales.groupby('Product')['Revenue'].sum().sort_values(ascending=False)
product_sales.to_excel('product_report.xlsx')