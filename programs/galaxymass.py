import numpy as np
from scipy.integrate import quad
import matplotlib.pyplot as plt

# density in solar masses per cubic kiloparsec, at 8kpc (solar radius)
rho0 = 4e7 
# scale radius of galaxy in kpc
hr = 3.2
# solar radius in kpc
r0 = 8 

def local_density(r):
    return rho0 * np.exp(-(r-r0)/hr)
local_density = np.vectorize(local_density)

# function to integrate over. additional r^2 sin(theta) for jacobian in 
# spherical. the sin(theta) is broken up and calcuated independently. 
f = lambda r: local_density(r) * np.square(r)

# fake triple integral. 4pi comes from integration of sin(theta) from 0 to pi
# (for theta), and integration of 1 from 0 to 2pi (for phi)
def menc(r):
    return quad(f, 0, r)[0] * 4*np.pi
menc = np.vectorize(menc)

# volume of sphere with radius r
def vol(r):
    return 4/3 * np.pi * np.power(r, 3)
vol = np.vectorize(vol)

# mean density of sphere of radius r
def mean_density(r):
    return menc(r) / vol(r)
mean_density = np.vectorize(mean_density)

x = np.arange(40)
y1 = local_density(x)
y2 = menc(x)
y3 = mean_density(x)


fig, ax = plt.subplots(3, sharex=True, figsize=(12, 12))
ax[0].plot(x, y1)
ax[0].set_title('local density')
ax[0].set_ylabel('$M_\odot\,kpc^{-3}$')
ax[1].plot(x, y2)
ax[1].set_title('mass enclosed')
ax[1].set_ylabel('$M_\odot$')
ax[2].plot(x, y3)
ax[2].set_title('mean density')
ax[2].set_ylabel('$M_\odot\,kpc^{-3}$')
plt.xlabel('distance from center of galaxy (kpc)')
plt.show()

