def logseries(k, p):
 return -p**k/(k*np.log(1-p))
centres = np.arange(1, max(s) + 1)
plt.plot(centres, logseries(centres, a) * s.size, 'r', label='logseries PMF')
plt.legend()
plt.show()