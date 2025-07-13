import matplotlib.pyplot as plt
x = np.linspace(0, 3, 50)
pdf = a / (x+1)**(a+1)
plt.hist(s, bins=x, density=True, label='histogram')
plt.plot(x, pdf, linewidth=2, color='r', label='pdf')