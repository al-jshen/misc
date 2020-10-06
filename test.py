import numpy as np
import matplotlib.pyplot as plt

for i in range(10):
    print("asdf")


def test(x, y):
    """Function definition.
    Calculates some stuff."""
    return np.power(np.log(x), np.exp(y))


x = np.arange(1, 11)
y = np.logspace(1e-5, 1e-3, 10)
z = test(x, y)

plt.scatter(x, z)
plt.show()
