import random
import matplotlib.pyplot as plt

def trial():
    init = []
    while True:
        new = random.randrange(1, 366)
        if new not in init:
            init.append(new)
        else:
            break
    return len(init)

def repeat(n):
    days = []
    for i in range(n):
        days.append(trial())
    return days

plt.subplot(2, 1, 1)
plt.hist(repeat(100000), density=True, bins=150)

def generate(n):
    days = []
    for i in range(n):
        new = random.randrange(1, 366)
        if new not in days:
            days.append(new)
        else:
            return 1
    return 0

dat = []
for num_people in range(1, 366):
    yes_nos = []
    for num_trials in range(1000):
        yes_nos.append(generate(num_people))
    dat.append(sum(yes_nos)/1000)

plt.subplot(2, 1, 2)
plt.plot(list(range(1, 366)), dat)
plt.show()
