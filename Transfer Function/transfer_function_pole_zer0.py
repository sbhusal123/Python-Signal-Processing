from scipy import signal
import numpy as np
import matplotlib.pyplot as plt
import matplotlib


def find_zeros_poles(numerator, denominator):
    # calculate zeros, poles and gain
    zeros, poles , gain = signal.tf2zpk(numerator, denominator)

    # rounding to 2 decimal place
    zeros = np.round(zeros, 3)
    poles = np.round(poles, 3)

    return zeros, poles

def plot_zeros_poles(zeros, poles):

    # find x,y for unit circle
    x = np.linspace(-1, 1, 1000)
    y = (1 - x * x) ** (0.5)

    # set size of figure
    matplotlib.rc('figure', figsize=(6.5, 6.5))

    # plotting unit circle
    plt.plot(x, y, '--g', label="Unit circle")
    plt.plot(x, -y, '--g',)

    # plotting zeros and poles
    plt.scatter(np.real(zeros) , np.imag(zeros), label='zeros' ,marker='o')
    plt.scatter(np.real(poles) , np.imag(poles), label='poles', marker='X')

    # set legend location
    plt.legend(loc='upper left')

    # set x label and y label
    plt.xlabel('Real(Z)', fontdict={'color':'r', 'size':15})
    plt.ylabel('Imag(Z)',  fontdict={'color':'r', 'size':15})
    plt.grid()


"""
Given transfer function is
H(z) = (z ^ 2 + 0.1 * z - 0.12) / (z ^ 2 - 0.5 * z + 0.2)
"""


# numerator and denominator coefficients
numerator = [1, 0.1, -0.12]
denominator = [1, -0.5, 0.2]

zeros, poles = find_zeros_poles(numerator, denominator)

# print zeros
print("Zeros are:")
for z in zeros:
    print(z)

# print poles
print('\nPoles are:')
for p in poles:
    print(p)

plot_zeros_poles(zeros, poles)
plt.title('Pole-zero plot',  fontdict={'color':'indigo', 'size':20})
plt.show()