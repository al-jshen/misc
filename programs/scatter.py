import numpy as np
import matplotlib.pyplot as plt
plt.style.use('dark_background')

n = 750
x = np.random.randint(0, 100, n)
y = np.random.randint(0, 100, n)
r = np.random.randint(0, np.pi*np.square(8), n)
c = ["#%02x%02x%02x" % (int(r), int(g), 200) for r, g in zip(2.5*x, 2.5*y)]
plt.figure(figsize=(10, 6))
plt.scatter(x, y, s=r, c=c, alpha=0.6)
plt.show()
