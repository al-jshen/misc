import numpy as np
import matplotlib.pyplot as plt

k=100
n=10000

dat = np.zeros(n-k)

for m in np.arange(n-k):
    dat[m] = np.math.factorial(n-k) * np.math.factorial(n-m) / ( np.math.factorial(n) * np.math.factorial(n-k-m) )

print(dat)

plt.plot(np.arange(n-k), dat)
plt.axhline(0.1)
plt.show()
