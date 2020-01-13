# rational roots checker
from pprint import pprint
import pandas as pd
import numpy as np

coeffs = list(map(int, input().split()))
deg = len(coeffs) - 1
first = abs(coeffs[0])
last = abs(coeffs[-1])

m_cands = [i for i in list(range(-last, 0)) + list(range(1, last+1)) if last % i == 0]
n_cands = [i for i in list(range(-first, 0)) + list(range(1, first+1)) if first % i == 0]

def poly(x):
    for i in range(deg+1):
        s = 0
        s += coeffs[i] * x**(deg-i)
        return s

df = pd.DataFrame(index=m_cands, columns=n_cands)

for idxm, m in enumerate(m_cands):
    for idxn, n in enumerate(n_cands):
        df.loc[m, n] = poly(m/n)
        
print(df)
