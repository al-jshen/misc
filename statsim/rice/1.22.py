import numpy as np
from math import factorial as f
from scipy.misc import comb as c
import matplotlib.pyplot as plt

dat = np.zeros(10)

for i in np.arange(1, 11):
    dat[i-1] = (f(40) / f(40-i)) / c(N=52, k=i, exact=True)

print(dat)
plt.plot(np.arange(10), dat)
plt.axhline(y=0.5, c='r')
plt.show()
