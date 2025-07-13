from scipy import stats
rvs = np.random.power(5, 1000000)
rvsp = np.random.pareto(5, 1000000)
xx = np.linspace(0,1,100)
powpdf = stats.powerlaw.pdf(xx,5)