import numpy as np
import matplotlib.pyplot as plt

n = 50
p = 0.10
import pandas as pd

class DiscreteRandomVariable:
    def __init__(self, a=0, b=1):
        self.variableType = ""
        self.low = a
        self.high = b
        return
    def draw(self, numberOfSamples):
        samples = np.random.random_integers(self.low, self.high, numberOfSamples)
        return samples

class BinomialRandomVariable(DiscreteRandomVariable):
    def __init__(self, numberOfTrials = 10, probabilityOfSuccess = 0.5):
        self.variableType = "Binomial"
        self.numberOfTrials = numberOfTrials
        self.probabilityOfSuccess = probabilityOfSuccess
        return
    def draw(self, numberOfSamples):
        samples = np.random.binomial(self.numberOfTrials, self.probabilityOfSuccess, numberOfSamples)
        return samples

X = BinomialRandomVariable(n, p)
X_samples = X.draw(10000)
Z_samples = (X_samples - n*p) / np.sqrt(n*p*(1-p))

plt.figure()
plt.subplot(211)
plt.hist(X_samples, bins=40)

plt.subplot(212)
plt.hist(Z_samples, bins=40)

plt.show()
