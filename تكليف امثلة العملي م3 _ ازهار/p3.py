import matplotlib.pyplot as plt

market_share = [130, 70, 78]
labels = ['Apple', 'Samsung', 'Huawei']  # <-- تعريف labels كقائمة صحيحة
sales = [120, 200, 80]

plt.pie(market_share, labels=labels, autopct='%1.0f%%')
plt.title("Mobile Phone Market Share")
plt.show()
