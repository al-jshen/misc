import numpy as np
import matplotlib.pyplot as plt

def l(x):
    return np.exp(-np.square(x-1)/2) + 3*np.exp(-np.square(x-2)/2)

x = np.linspace(-10, 10)
y = l(x)

print(x[np.argmax(y)])

plt.plot(x, y)
plt.show()
