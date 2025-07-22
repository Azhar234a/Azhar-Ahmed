from statistics import mean
import matplotlib.pyplot as plt
x=["lst Quarter","2nd Quarter","3rd Quarter","4th Quarter"]
y=[130,135,140,160]
plt.plot(x,y, marker='o',color='blue')
mean_y = mean(y)
max_y = max(y)
print("Mean of Sales:" , mean_y)
print("Mean of Sales:" , max_y)
plt.axhline(mean_y, color='r', linestyle=':')
plt.annotate('Peak(Maximum) Sales' , xy=(4,160), xytext=(3,140),
           arrowprops=dict(facecolor='black', shrink=0.05))
plt.title("Quarterly sales")
plt.xlabel("Quarter")
plt.ylabel("Sales ($ Thousands)")
plt.grid()
plt.show()