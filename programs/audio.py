import sounddevice as sd
import numpy as np
import matplotlib.pyplot as plt


def gen_freqax(duration):
    recording = sd.rec(int(duration * fs), samplerate=fs, channels=2)
    sd.wait()
    d = np.fft.rfft(recording[:, 0])
    freq = np.fft.fftfreq(d.size, 1 / fs)
    return freq


def gen_spec(duration):
    recording = sd.rec(int(duration * fs), samplerate=fs, channels=2)
    sd.wait()
    d = np.fft.rfft(recording[:, 0])
    specpow = np.abs(d)
    return specpow


if __name__ == "__main__":
    fs = 81000
    dur = 0.05

    plt.ion()
    fig = plt.figure()
    ax = fig.add_subplot(111)

    x = gen_freqax(dur)
    y = gen_spec(dur)
    plt.xscale("log")
    plt.xlim(0, 1e5)
    plt.ylim(0, 50)
    (p,) = plt.plot(x, y)

    while True:
        s = gen_spec(dur)
        p.set_ydata(s)
        fig.canvas.draw()
        fig.canvas.flush_events()
