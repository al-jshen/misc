import numpy as np

def trial():
    init = 0
    while init < 11:
        init += np.random.randint(1, 3)
        if init == 3 or init == 6:
            return 0
        elif init == 10:
            return 1
    return 0

n_trials = 100000
counter = 0
for i in range(n_trials):
    counter += trial()

print(counter / n_trials)
