import numpy as np
import matplotlib.pyplot as plt

trials = 10000
count = 0
probs = np.zeros(trials)
possible_doors = np.arange(1, 4)

for i in np.arange(trials):
    # you pick a random door initially
    chosen_door = np.random.choice(possible_doors)
    # car is behind a random door
    car_door = np.random.choice(possible_doors)
    # monty picks the door that you didnt choose and that doesnt have a car
    monty_door = np.random.choice([i for i in possible_doors if i not in [chosen_door, car_door]])
    # you switch doors 
    switched_door = [j for j in possible_doors if j not in [monty_door, chosen_door]][0]

    if switched_door == car_door:
        count += 1
    probs[i] = count/(i+1)

losses = abs(probs - 2/3)

fig, axes = plt.subplots(2, figsize=(12, 8))
fig.suptitle('Monty Hall Problem')

axes[0].plot(np.arange(trials), losses)
axes[0].plot([0, trials], [0, 0], c='r')
axes[0].set_title('Loss')

axes[1].plot(np.arange(trials), probs)
axes[1].plot([0, trials], [2/3, 2/3], c='r')
axes[1].set_title('Convergence to Result')
plt.show()

