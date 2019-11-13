import numpy as np
import matplotlib.pyplot as plt
from scipy.io import wavfile as wav
from scipy import fftpack

filepath = ''
rate, dat = wav.read(filepath)
fft_out = fftpack.fft(dat)
freqs = fftpack.fftshift(dat)*rate

threshold = 700
higher = [(i, j) for i,j in zip(freqs, np.abs(fft_out)) if j > threshold and i > 0]
higher.sort()
print(higher)

plt.plot(freqs, np.abs(fft_out))
plt.xlim(left=0, right=8000)
# plt.xscale('log')
plt.show()
