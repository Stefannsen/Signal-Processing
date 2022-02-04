# Negulescu Stefan, 332

import numpy as np
import matplotlib.pyplot as plt

# 1
"""
f = fs / N
f = 1 Hz
fs = 44.1 kHz = 44100 Hz 
=>
N = fs / f = 44100 samples

"""

# 2

# a)

# Window functions


def rectangular_window(N):
    arr = [1 for i in range(N)]
    return arr


def hanning_window(N):
    arr = [0.5 * (1 - np.cos(2 * np.pi * i / N)) for i in range(N)]
    return arr


def hamming_window(N):
    arr = [0.54 - 0.46 * np.cos(2 * np.pi * i / N) for i in range(N)]
    return arr


def blackman_window(N):
    arr = [0.42 - 0.5 * np.cos(2 * np.pi * i / N) + 0.08 * np.cos(4 * np.pi * i / N) for i in range(N)]
    return arr


def flattop_window(N):
    arr = [0.22 - 0.42 * np.cos(2 * np.pi * i / N) + 0.28 * np.cos(4 * np.pi * i / N)
           - 0.08 * np.cos(6 * np.pi * i / N) + 0.007 * np.cos(8 * np.pi * i / N)
           for i in range(N)]
    return arr


def sine(amplitude, frequency, phase, time):
    return amplitude * np.cos(2*np.pi*frequency*time + phase)


def plot_window(window_function):
    plt.plot(time[:200], signal[:200])
    plt.grid("True")
    plt.show()

    plt.plot(time[:200], signal[:200] * window_function(200))
    plt.grid("True")
    plt.show()


def plot_fft(sine, window_function):
    signal = window_function(1000) * sine[:1000]
    fft = abs(np.fft.fft(signal))
    plt.plot(time[:500], fft[:500])
    plt.grid("True")
    plt.show()


f = 100
A = 1
phi = 0
time_of_view = 1
n_samples = 1000

time = np.linspace(0, time_of_view, n_samples)
signal = sine(A, f, phi, time)

# PLOT SIGNAL + WINDOW
plot_window(rectangular_window)
# plot_window(hamming_window)


# b)

time = np.linspace(0, 1, 8000)
signal_A = sine(A, 1000, phi, time)
signal_B = sine(A, 1100, phi, time)

# rectangular_window este mai potrivita pentru signal_A deoarece reduce fenomenul de leakage

# PLOT FFT
# plot_fft(signal_A, rectangular_window)
# plot_fft(signal_B, rectangular_window)


# c)
# PLOT SIGNAL + WINDOW (celelalte functii window)
# plot_window(hamming_window)
# plot_window(blackman_window)
# plot_window(flattop_window)


# 3
"""
Am facut acest exercitiu la lab2(BONUS).
"""
