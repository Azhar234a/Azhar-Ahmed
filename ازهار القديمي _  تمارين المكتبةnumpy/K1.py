a = .6
rng = np.random.default_rng()
s = rng.logseries(a, 10000)
import matplotlib.pyplot as plt
bins = np.arange(-.5, max(s) + .5 )
count, bins, _ = plt.hist(s, bins=bins, label='Sample count')
