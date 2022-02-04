import csv
import numpy as np
import matplotlib.pyplot as plt
import scipy.signal

# 1


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


time = np.linspace(0, 1, 100)
time2 = np.linspace(0, 504/3600, 504)
time3 = np.linspace(0, 504, 504)


def plot_fft(window_function):
    signal = window_function(100)
    fft = abs(np.fft.fft(signal))
    plt.plot(time[:50], fft[:50])
    plt.grid("True")
    plt.show()


"""
plot_fft(rectangular_window)
plot_fft(hanning_window)
plot_fft(hamming_window)
plot_fft(blackman_window)
plot_fft(flattop_window)
"""

# 2

with open('trafic.csv', newline='') as f:
    reader = csv.reader(f)
    data = list(reader)
data[0][0] = data[0][0][3:]
dataList = []
for x in data:
    dataList.append(int(x[0]))
# print(dataList) len = 504

# a)

fft = abs(np.fft.fft(dataList))
plt.plot(time2[:252], fft[:252])
plt.grid("True")
plt.show()

# b)
# Frecventa de taiere este una joasa deoarece vreau sa observ trendul pe fiecare saptamana.
# De asemenea voi include toate frecventele cu amplitudine mare.
# Astfel, voi alege spre exemplu cutoffFreq = 0.02 Hz.

# f = 1/T
# Ts = 1h = 3600 s => fs = 1 / 3600 Hz
# fNyquist = fs / 2 => fNyquist = 1 / 7200 Hz
# cutoffFreq = 0.02 / fNyquist = 0.014 (normalizata in [0, 1])


# c)
butter_b, butter_a = scipy.signal.butter(5, 0.014, btype='low')
chebyshev_b, chebyshev_a = scipy.signal.cheby1(5, 5, 0.014, btype='low')

# d)
butter_w, butter_h = scipy.signal.freqz(butter_b, butter_a)
chebyshev_w, chebyshev_h = scipy.signal.freqz(chebyshev_b, chebyshev_a)


plt.plot(butter_w, 20 * np.log10(abs(butter_h)), label='butter_ans')
plt.plot(chebyshev_w, 20 * np.log10(abs(chebyshev_h)), label='chebyshev_ans')
plt.grid("True")
plt.legend()
plt.show()

# e)
# Filtrul mai potrivit pare a fi filtrul Butterworth, deoarece reprezinta mai clar diferentele intre saptamani,
# pastrand si amplitudinea mai mare fata de filtrul Chebyshev.

butter_filtered = scipy.signal.filtfilt(butter_b, butter_a, dataList)
chebyshev_filtered = scipy.signal.filtfilt(chebyshev_b, chebyshev_a, dataList)
plt.plot(time3, dataList, label='original')
plt.plot(time3, butter_filtered, label='butter-filtered')
plt.plot(time3, chebyshev_filtered, label='chebyshev-filtered')
plt.grid("True")
plt.legend()
plt.show()


# f)
# Butterworth:
# Un ordin prea mic (de exemplu 1) pastreaza in continuare informatie de care nu am nevoie,
# deoarece ma intereseaza trendul saptamnal si mai putin trendul pe zile.
# In acelasi timp, o valoare prea mare a ordinului (ex 6) deformeaza realitatea.
# O valoare optima pt ordinul filtrului Butterworth este 3.
# Chebyshev:
# Cand ordinul este o valoare mica (ex 1), este pastrata prea multa informatie.
# Daca ordinul creste, iar rp-ul pastreaza o valoare scazuta, filtrul se comporta ca unul Butterworth, fiind diferente
# mici intre amplitudinile pastrate dupa filtrare.
# In concluzie, un filtru bun pentru acest caz ramane Butterworth de ordin 3.
butter_b, butter_a = scipy.signal.butter(4, 0.014, btype='low')
chebyshev_b, chebyshev_a = scipy.signal.cheby1(3, 2, 0.014, btype='low')
butter_filtered = scipy.signal.filtfilt(butter_b, butter_a, dataList)
chebyshev_filtered = scipy.signal.filtfilt(chebyshev_b, chebyshev_a, dataList)
plt.plot(time3, dataList, label='original')
plt.plot(time3, butter_filtered, label='butter-filtered')
plt.plot(time3, chebyshev_filtered, label='chebyshev-filtered')
plt.grid("True")
plt.legend()
plt.show()
