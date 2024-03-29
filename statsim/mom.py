"""
Start with $4
Play $1 bets
If win, then double bet
    If win the second bet, then count as WIN and leave
If lose, then next bet is $1
Repeat until no more money, then count as LOSE
"""

import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

n_trials = 100000
n_wins = 0
n_money = []
n_ties = 0

for i in range(n_trials):
    money = 4
    bet = 1
    while money > 0:
        # random binary condition generator
        if (not np.random.choice((0, 1))): # win first time
            money += bet
            bet *= 2 # double the next bet
            #print(f'won first bet, at {money}, bet is {bet}')
            if (not np.random.choice((0, 1))): # won twice in a row
                if money == 4: # break even
                    n_ties += 1
                    break
                money += bet # add money
                n_wins += 1 # log win
                n_money.append(money) # log cash at end of game
                #print(f'won game, at {money}')
                break
            else:
                money -= bet
                bet = 1
                #print(f'lost second bet, at {money}, bet is {bet}')
        else:
            money -= bet
            #print(f'lost first bet, at {money}, bet is {bet}')

print(n_wins/n_trials*100)
print(np.mean(n_money))
print(n_ties/n_trials*100)
print((1-(n_wins+n_ties)/n_trials)*100)
#sns.distplot(n_money)
#plt.show()
