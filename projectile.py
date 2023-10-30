import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import minimize_scalar

# Initial conditions
v0 = 10.0  # m/s
x0 = 0.0  # m
y0 = 0.0  # m
g = 9.81  # m/s^2
dt = 0.0000001  # s

fig, ax = plt.subplots(1, 2)

# find the largest angle theta such that the minimum of drdt is as close to 0 as possible


def _inner_opt(theta_deg):
    theta = np.deg2rad(theta_deg)

    # Create arrays
    t = []
    x = []
    y = []

    # initial step
    t.append(0.0)
    x.append(x0)
    y.append(y0)

    # first step
    t.append(dt)
    x.append(x0 + v0 * t[1] * np.cos(theta))
    y.append(y0 + v0 * t[1] * np.sin(theta) - 0.5 * g * t[1] ** 2)

    # keep stepping until y < 0 (i.e. the projectile hits the ground)
    while y[-1] >= 0:
        t.append(t[-1] + dt)
        x.append(x[-1] + v0 * dt * np.cos(theta))
        y.append(y[-1] + v0 * dt * np.sin(theta) - 0.5 * g * t[-1] ** 2)

    t = np.asarray(t)
    x = np.asarray(x)
    y = np.asarray(y)
    r = np.sqrt(x**2 + y**2)

    drdt = np.diff(r) / dt

    return x, y, drdt


def inner_opt(theta_deg):
    _, _, drdt = _inner_opt(theta_deg)
    return np.min(drdt) ** 2


res = minimize_scalar(
    inner_opt,
    bounds=(0, 90),
    method="bounded",
    options={"disp": 3},
)

print(res)

# find the angle theta that minimizes the minimum of drdt

for theta in np.linspace(0, 90, 20):
    x, y, drdt = _inner_opt(theta)

    ax[0].plot(x, y, label=f"{theta:.1f}")
    ax[0].set_xlabel("x")
    ax[0].set_ylabel("y")

    ax[1].plot(drdt, label=f"{theta:.1f}")
    ax[1].set_xlabel("t")
    ax[1].set_ylabel("dr/dt")

x, y, drdt = _inner_opt(res.x)
ax[0].plot(x, y, label=f"{res.x:.2f}", c="k", lw=2)
ax[0].set_xlabel("x")
ax[0].set_ylabel("y")

ax[1].plot(drdt, label=f"{res.x:.2f}", c="k", lw=2)
ax[1].set_xlabel("t")
ax[1].set_ylabel("dr/dt")

ax[0].axhline(y=0, color="gray")
ax[1].axhline(y=0, color="gray")
ax[0].legend()
ax[1].legend()

plt.show()
