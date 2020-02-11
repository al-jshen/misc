import numpy as np
import matplotlib.pyplot as plt

def logistic(r, x):
    return r*x*(1-x)

def sim(r, x, n):
    dat = np.zeros(n)
    dat[0] = x
    for i in np.arange(1, n):
        dat[i] = logistic(r, dat[i-1])
    return dat

# play with this line!
rs = np.linspace(2, 3, 10)

for r in rs:
    d = sim(r, 0.5, 100)
    plt.plot(d)

plt.show()

