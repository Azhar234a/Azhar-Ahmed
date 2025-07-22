import matplotlib.pyplot as plt
from statistics import mean

x = ["Q1", "Q2", "Q3", "Q4"]
y = [130, 135, 140, 160]

plt.plot(x, y)
plt.axhline(mean(y), color='red', linestyle='--')
plt.title("Quarterly Sales with Mean Line")
plt.xlabel("Quarter")
plt.ylabel("Sales ($K)")
plt.savefig("quarterly_sales.png", dpi=300)
