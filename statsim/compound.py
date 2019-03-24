import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
from collections import OrderedDict

# prevent scientific notation in dataframe, round to 2 decimal places
pd.set_option('display.float_format', lambda x: '%.2f' % x)
plt.style.use('dark_background')

trials = 5
time_length=20
min_interest = 1
max_interest = 8
volatility=11
contributions = [i*10000 for i in [3, 4, 5, 6, 7, 8, 9, 10]]
interest_rates = np.arange(min_interest, max_interest+0.1, 1)

def run_trial(shock=True, contribution=10000, principal=0, volatility=10, time_length=20):

    di = {}

    for rate in interest_rates:
        prices = np.zeros(time_length)
        prices[0] = principal

        for i in np.arange(1, time_length, 1):
            prices[i] = (prices[i-1] + contribution) * (1 + rate/100)
            if shock:
                prices[i] *= (np.random.normal(1, volatility/100))

        di[rate] = prices

    return di

dat = {amount:[run_trial(shock=True, contribution=amount, principal=20000, volatility=volatility) for i in range(trials)] for amount in contributions}

average_returns = []
# for each contribution amount, calculate return for each rate, averaged over all trials
for idx1, contrib in enumerate(contributions): # for each contribution amount
    this_contrib = []
    for idx2, all_trials in enumerate(dat[contrib]): # average over all trials
        this_trial = []
        for idx3, rates in enumerate(interest_rates): # for each rate
            this_trial.append(dat[contrib][idx2][rates][-1])
        this_contrib.append(this_trial)
    average_returns.append(this_contrib)

average_returns = np.array(average_returns).mean(1) # average of dim2 (trials)
ar = pd.DataFrame(average_returns)
ar.columns = interest_rates
ar.columns.names = ['Rates']
ar.index = contributions
ar.index.names = ['Contribution Amounts']

print(ar)

fig, axes = plt.subplots(len(contributions), figsize=((12, 24)))

for idx, (contrib_key, contrib_value) in enumerate(dat.items()):
    for trial in contrib_value:
        for rate_key, rate_value in trial.items():
            sns.lineplot(data=rate_value, ax=axes[idx], label=f'At {rate_key}%: ${ar.loc[contrib_key, rate_key]:,.2f} Average Return')
        # Reset colour cycle
        axes[idx].set_prop_cycle(None)

        # remove duplicates in the legend
        handles, labels = axes[idx].get_legend_handles_labels()
        by_label = OrderedDict(zip(labels, handles))
        axes[idx].legend(by_label.values(), by_label.keys(), title=f'${contrib_key:,.2f} Yearly Contribution\n')


plt.suptitle(f'Monte Carlo Simulation (n={trials}) of Possible Returns Over {time_length} Years at {volatility}% Volatility')
plt.show()
