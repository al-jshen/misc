from mpl_toolkits import mplot3d
import numpy as np
import matplotlib.pyplot as plt


ax = plt.axes(projection='3d')
x = np.linspace(0, 6, 100)

for i in x:
    y = np.linspace(0, (6-i)/2)
    x2 = np.full(y.shape, i)
    z = (6-x2-2*y)/3
    ax.plot(x2, y, z, c='b')
    print(*zip(x2, y, z))

plt.plot((0, 1), (0, 2), (0, 3), c='r')
ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_zlabel('z')
plt.show()

