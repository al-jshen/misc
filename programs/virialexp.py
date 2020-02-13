import numpy as np

r = 8.31
p = 1.013e5

def vn(t, b):
    term1 = r*t
    term2 = np.sqrt( np.square(r*t) - 4*p*(-r*t*b))
    denom = 2*p
    return (term1 + term2) / denom, (term1 - term2) / denom

ts = np.arange(100, 601, 100)
bs = np.array([-160, -35, -4.2, 9, 16.9, 21.3]) * 1e-6

print(bs / vn(ts, bs)[0])
