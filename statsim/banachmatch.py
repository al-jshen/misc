import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

def trial(n=10):
    left = n
    right = n
    while True:
        if np.random.randint(2) == 0:
            if left == 0:
                return right
            left -= 1
        else:
            if right == 0:
                return left
            right -= 1


n_trials = 10000
dat = np.zeros(n_trials)
n = 30

for i in np.arange(n_trials):
    dat[i] = trial(n=n)

val, ct = np.unique(dat, return_counts=True)
c = ct / n_trials
for i in zip(val, c):
    print(i)

sns.distplot(dat, kde=False)
plt.title(f'Distribution for n={n}')
plt.show()
