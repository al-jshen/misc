import numpy as np
import matplotlib.pyplot as plt

n = 30
l = 5
trials = 100000

def score(dat, l):
    return dat.size*(dat.mean() - l) / l

def sample(l, n):
    return np.random.poisson(l, n)

d = np.zeros(trials)
for i in np.arange(trials):
    d[i] = score(sample(l, n), l)
print(d.mean(), d.var())
plt.hist(d)
plt.show()

