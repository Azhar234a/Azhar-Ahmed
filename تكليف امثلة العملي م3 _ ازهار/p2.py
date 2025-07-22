import matplotlib.pyplot as plt
products = ['Laptop', 'phone', 'Tablet']
sales = [120, 200, 80]
plt.bar(products, sales, color=['blue', 'green', 'red'])
plt.title("Product sales")
plt.ylabel("Quantity Sold")
plt.show()