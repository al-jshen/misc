from mpl_toolkits import mplot3d
import numpy as np
import matplotlib.pyplot as plt


ax = plt.axes(projection='3d')
x = np.linspace(-1, 1)
y = np.linspace(-1, 1)
X, Y = np.meshgrid(x, y)
Z = np.sqrt(1 - np.square(X) - np.square(Y))
ax.plot_surface(X, Y, Z)
ax.plot_surface(X, Y, -Z)
ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_zlabel('z')
plt.show()

