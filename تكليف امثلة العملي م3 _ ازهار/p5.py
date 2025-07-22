import matplotlib.pyplot as plt

x = ["Q1", "Q2", "Q3", "Q4"]
y = [130, 135, 140, 160]
products = ["Laptop", "Phone", "Tablet"]
sales = [120, 200, 80]
labels = ["Apple", "Samsung", "Huawei"]
market_share = [130, 70, 78]

fig, axs = plt.subplots(1, 3, figsize=(15, 5))

# Line plot
axs[0].plot(x, y)
axs[0].set_title("Line Plot")

# Bar chart
axs[1].bar(products, sales)
axs[1].set_title("Bar Chart")

# Pie chart
axs[2].pie(market_share, labels=labels, autopct='%1.1f%%')
axs[2].set_title("Pie Chart")

plt.tight_layout()
plt.show()
