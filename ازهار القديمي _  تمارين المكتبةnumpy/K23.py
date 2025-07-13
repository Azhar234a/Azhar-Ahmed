dfnum = 3 # between group deg of freedom
dfden = 20 # within groups degrees of freedom
nonc = 3.0
nc_vals = np.random.noncentral_f(dfnum, dfden, nonc, 1000000)
NF = np.histogram(nc_vals, bins=50, density=True)
c_vals = np.random.f(dfnum, dfden, 1000000)
F = np.histogram(c_vals, bins=50, density=True)
import matplotlib.pyplot as plt
plt.plot(F[1][1:], F[0])
plt.plot(NF[1][1:], NF[0])
plt.show()