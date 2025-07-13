def logseries(k, p):
return -p**k/(k*np.log(1-p))
plt.plot(bins, logseries(bins, a)*count.max()/
logseries(bins, a).max(), 'r')
plt.show()