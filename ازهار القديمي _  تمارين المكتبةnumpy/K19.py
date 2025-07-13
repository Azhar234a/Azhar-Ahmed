b = np.array(b) / np.min(b) # scale values to be positive
count, bins, ignored = plt.hist(b, 100, density=True, align='mid')
sigma = np.std(np.log(b))
mu = np.mean(np.log(b))
