import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

for dim in range(1, 100, 10):
    dat = np.random.multivariate_normal(np.zeros(dim), np.eye(dim), size=int(1e3))
    norms = np.linalg.norm(dat, axis=1) / np.sqrt(dim)
    # plt.scatter(dim, norms.mean(), c="b")
    # plt.scatter(dim, norms.std(), c="r")
    sns.kdeplot(norms, label=dim)
plt.legend()
plt.show()
