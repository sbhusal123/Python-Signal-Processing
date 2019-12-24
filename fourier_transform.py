import numpy as np
import matplotlib.pyplot as plt
from scipy.fftpack import fft


sampling_per_second = 100
T = 3
f1 = 10
f2 = 20
t = np.linspace(0, T, T * sampling_per_second + 1)

signal1 = np.sin(2 * np.pi * f1 * t)
signal2 = np.sin(2 * np.pi * f2 * t)
superposed_signal = signal1 + signal2

fft_points = fft(superposed_signal)
magnitude = np.abs(fft_points)

fig = plt.figure()

plt.subplot(2,2,1)
plt.plot(t, signal1, '-r')
plt.title(f'{f1}Hz signal')

plt.subplot(2,2,2)
plt.plot(t, signal2, '-b')
plt.title(f'{f2}Hz signal')

plt.subplot(2,2,3)
plt.plot(t, superposed_signal, '-g')
plt.title('Superposed signal')

plt.subplot(2,2,4)
f = np.linspace(0,sampling_per_second/2, 150)
plt.plot(f, magnitude[0:150], '-y')
plt.title('FFT plot')

plt.subplots_adjust(hspace=0.7)
plt.show()