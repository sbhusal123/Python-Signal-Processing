import numpy as np
import matplotlib.pyplot as plt
from scipy import signal

"""
Given transfer function is
H(z) = (z ^ 2 + 0.1 * z - 0.12) / (z ^ 2 - 0.5 * z + 0.2)
"""
numerator = [1, 0.1, -0.12] # numerator coefficients
denominator = [1, -0.5, 0.2] # denominator coefficients


# calculating frequency response
w, h = signal.freqz(numerator, denominator, whole=True)

# round the frequency values to 3 decimal place
h = np.round(h, 3)

# magnitude in dB
h_db = 20*np.log10(np.abs(h))

# plot magnitude response
plt.subplot(2,1,1)
plt.plot(w, h_db)
plt.xlabel(r'$\Omega$  (1 Unit= $ \frac{\pi}{3}$)', fontdict={'size': 15, 'color': 'indigo'})
plt.ylabel(r'$|H(\Omega)| dB$', fontdict={'size': 15, 'color': 'indigo'})
plt.title('Amplitude response', fontdict={'size':15, 'color': 'red'})
plt.grid()


# phase
h_angle = np.angle(h)

# plot phase response
plt.subplot(2,1,2)
plt.plot(w, h_angle)
plt.xlabel(r'$\Omega$  (1 Unit= $ \frac{\pi}{3}$)', fontdict={'size': 15, 'color': 'indigo'})
plt.ylabel(r'$\angle H(\Omega)$', fontdict={'size': 15, 'color': 'indigo'})
plt.title('Phase response', fontdict={'size':15, 'color': 'red'})
plt.grid()

plt.subplots_adjust(hspace=0.6)
plt.show()