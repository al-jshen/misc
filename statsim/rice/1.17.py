# Rice Chapter 1 Question 17

import numpy as np
import matplotlib.pyplot as plt

n_trials = 10000
dat = np.zeros(101)

for perc in np.arange(101):
    # let 1 be defective
    samples = np.random.choice([0, 1], p=[1-perc/100, perc/100], size=(4, n_trials))
    smashed = samples.sum(axis=0)
    # only want trials where all four sampled items were not defective
    n_accepted = np.count_nonzero(smashed==0)
    dat[perc] = n_accepted/n_trials

plt.plot(np.arange(101), dat)
plt.show()
