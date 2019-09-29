import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

current_palette = sns.color_palette('dark')

for i in range(1, len(current_palette)+1):
    sns.distplot(np.random.gamma(i, size=1000), hist=False, label=i)

plt.title('Gamma Distribution with Various Shape Parameters')
plt.show()
