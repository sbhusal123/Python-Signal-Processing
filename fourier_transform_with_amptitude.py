import numpy as np
from scipy.fftpack import fft
import matplotlib.pyplot as plt

# signal paramaters
T = 2
sample_per_second = 500 # more is the sample per second (sampling frequency) more accurate is plot
t = np.linspace(0, T, T * sample_per_second)

# signal 1
f1 = 1
a1 = 10
sig1 = a1*np.sin(2 * np.pi * f1 * t)

# plotting signal 1
plt.subplot(2, 2, 1)
plt.plot(t, sig1)
plt.title(f'{f1}Hz signal with  {a1} Amp')
plt.xlabel('time')
plt.ylabel('Amplitude')


# signal2
f2 = 10
a2 = 50
sig2 = a2*np.sin(2 * np.pi * f2 * t)

# plotting signal 2
plt.subplot(2, 2, 2)
plt.plot(t, sig2)
plt.title(f'{f2}Hz signal with {a2} Amp')
plt.xlabel('time')
plt.ylabel('Amplitude')


# superposing two signals
sig = sig1 + sig2

# plotting superposed signal
plt.subplot(2,2,3)
plt.plot(t, sig)
plt.title('Superposed signal')
plt.xlabel('time')
plt.ylabel('Amplitude')

# calculation of fft
sig1_freq = fft(sig)
fft_mag = np.abs(sig1_freq) 

# calculating amplitude 
fft_amp = (fft_mag) / (sample_per_second)

# rescaling frequency axis according to nyquist frequency
ff_freq = np.linspace(0, sample_per_second/2, sample_per_second)


# plot FFT diagram
plt.subplot(2, 2, 4)
plt.plot(ff_freq, fft_amp[0:sample_per_second], '-g')
plt.title('FFT of superposed signal with amplitude')
plt.xlabel('frequency')
plt.ylabel('Amplitde')


plt.subplots_adjust(hspace=0.7, wspace=0.3)
plt.grid()
plt.show()