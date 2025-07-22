import matplotlib.pyplot as plt
x=["lst Quarter","2nd Quarter","3rd Quarter","4th Quarter"]
y=[130,135,140,160]
plt.plot(x,y, marker='o',color='green', linestyle='--')
plt.title("Quarterly sales")
plt.xlabel("Quarter")
plt.ylabel("Sales ($ Thousands)")
plt.grid()
plt.show()
