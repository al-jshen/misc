import numpy as np
import matplotlib.pyplot as plt
import scipy.stats as stats


def get_bounds(mean, std, size, gamma):
    sample = np.random.normal(mean, std, size)
    xbar = sample.mean()
    lower = xbar - stats.norm.ppf((1 + gamma) / 2) * std / np.sqrt(size)
    upper = xbar + stats.norm.ppf((1 + gamma) / 2) * std / np.sqrt(size)
    capture = lower <= mean <= upper
    return lower, upper, capture


trials = 100
mean = 5
std = 4
size = 30
gamma = 0.95

for i in np.arange(trials):
    lower, upper, capture = get_bounds(mean, std, size, gamma)
    plt.plot([i, i], [lower, upper], c='b' if capture else 'r')
plt.axhline(mean)
plt.show()
