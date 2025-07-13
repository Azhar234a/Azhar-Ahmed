mu, kappa = 0.0, 4.0 # mean and concentration
rng = np.random.default_rng()
s = rng.vonmises(mu, kappa, 1000)
