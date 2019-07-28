"""
Real numbers between $0$ and $1$, inclusive, are chosen in the following manner.
A fair coin is flipped. If it lands heads, then it is flipped again 
and the chosen number is $0$ if the second flip is heads and $1$ 
if the second flip is tails. On the other hand, if the first coin flip is
tails, then the number is chosen uniformly at random from the closed 
interval $[0,1]$. Two random numbers $x$ and $y$ are chosen independently
in this manner. What is the probability that $|x-y| > \tfrac{1}{2}$?

2019 AMC 12A Q20
"""


import numpy as np

n_trials = 10000
results = np.zeros(n_trials)

def flip():
    if np.random.randint(2) == 0:
        if np.random.randint(2) == 0:
            return 0
        else:
            return 1
    else:
        return np.random.uniform()

def trial():
    return np.abs(flip() - flip())

for i in range(n_trials):
    results[i] = trial()

print(sum(results > 0.5) / n_trials)
    
