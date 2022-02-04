# Negulescu Stefan, 332

import numpy as np
import matplotlib.pyplot as plt
import csv


# 1
"""
Frecvente intre 40 si 200 Hz => fs > 2*200 = 400 Hz

"""

# 2
"""
Frecventa optima sub-Nyquist

B = 10 Hz
fc = 90 Hz

Conditii: 
1)  (2*fc-B)/m >= fs >= (2*fc+B)/(m+1)
2)  fs > 2B

a) m = 1
 (180-10)/1 >= fs >= (180+10)/2 <=> 170 >= fs >= 95 
 fs > 20                                            
 => 
 fs = 95 Hz (a.i. replicile sa fie centrate in 0)

b) m = 2
 (180-10)/2 >= fs >= (180+10)/3 <=> 85 >= fs >= 63.3
 fs > 20
 => 
 fs = 85 Hz (a.i. replicile sa fie centrate in 0)

c) m = 4
 (180-10)/4 >= fs >= (180+10)/5 <=> 42.5 >= fs >= 38
 fs > 20 
 =>  
 fs = 42.5 (a.i. replicile sa fie centrate in 0)

"""

# 3


def sine(amplitude, frequency, phase, time):
    return amplitude * np.cos(2*np.pi*frequency*time + phase)


f = 100
A = 1
phi = 0
time_of_view = 1
n_samples = time_of_view * 1000

# timpul pt semnalul continuu
atime = np.linspace(0, time_of_view, int(10**4/5))
# timpul pt semnalul discret
time = np.linspace(0, time_of_view, n_samples)
frequencies = np.linspace(0, 500, 500)


signalA = sine(A, f, phi, atime)
signalB = sine(A, 300, phi, time)
discreteA = sine(A, f, phi, time) + signalB

"""
fig = plt.figure()
plt.plot(atime, signalA)
#plt.stem(time, discreteA)
plt.grid("True")
plt.show()
"""

X = np.fft.fft(discreteA)
fig2 = plt.figure()
plt.stem(frequencies, X[:int(len(X)/2)])
plt.grid("True")
plt.show()


# 4

"""
def conv(window):
    dataListDays = dataList[:72 + window - 1]
    Y = np.convolve(dataListDays, np.ones(window), 'valid') / window
    return Y

# a)
with open('trafic.csv', newline='') as f:
    reader = csv.reader(f)
    data = list(reader)
data[0][0] = data[0][0][3:]
dataList = []
for x in data:
    dataList.append(int(x[0]))
print(dataList)


# b)
w = 1
samples = np.linspace(0, 3, 72)
Y = conv(1)
Y1 = conv(5)
Y2 = conv(7)
Y3 = conv(10)

fig3 = plt.figure()
plt.plot(samples, Y, label="w=1")
plt.plot(samples, Y1, label="w=5")
plt.plot(samples, Y2, label="w=7")
plt.plot(samples, Y3, label="w=10")
plt.legend()
plt.grid("True")
plt.show()

# c)
FFT = np.fft.fft(Y)
fig4 = plt.figure()
plt.stem(samples[:int(len(samples)/2)], FFT[:int(len(FFT)/2)])
plt.grid("True")
plt.show()
"""
