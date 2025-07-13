plt.figure()
plt.hist(rvs, bins=50, density=True)
plt.plot(xx,powpdf,'r-')
plt.title('power(5)')