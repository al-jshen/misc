import numpy as np
from matplotlib import pyplot as plt
import seaborn as sns

n_trials = 100000
n_flips = 1000
threshold = 800

data = np.random.randint(2, size=(n_trials, n_flips))
dist = data.sum(axis=1)
sns.distplot(dist)
plt.axvline(x=threshold)
print((dist > threshold).sum() / n_trials)
plt.show()

