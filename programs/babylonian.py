import random
import matplotlib.pyplot as plt
import numpy as np

radicand = int(input())
trials = 20
guesses = np.zeros(trials)
guess = random.randint(1, 100)

for i in range(trials):
    guess = (guess + radicand/guess) / 2
    guesses[i] = guess

loss = np.abs(np.sqrt(radicand) - guesses)
plt.plot(np.arange(trials), loss)
plt.plot([0, trials], [0, 0], c='r')
plt.show()
