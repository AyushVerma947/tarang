import numpy as np
import matplotlib.pyplot as plt

# Function to convolve two signals
def convolve_signals(signal1, signal2):
    return np.convolve(signal1, signal2, 'full')

# Input from the user
frequency1 = float(input("Enter the first frequency (in Hz): "))
frequency2 = float(input("Enter the second frequency (in Hz): "))

# Create time-domain signals for the input frequencies
fs = 1000  # Sampling frequency (Hz)
t = np.arange(0, 1, 1/fs)  # Time values from 0 to 1 second
signal1 = np.sin(2 * np.pi * frequency1 * t)
signal2 = np.sin(2 * np.pi * frequency2 * t)

# Convolve the two signals
convolved_signal = convolve_signals(signal1, signal2)

# Time values for the convolved signal
convolved_t = np.arange(0, len(convolved_signal)/fs, 1/fs)  # Adjusted time values

# Plot the original signals and the convolved signal
plt.figure(figsize=(12, 6))
plt.subplot(3, 1, 1)
plt.plot(t, signal1)
plt.title('Signal 1 (Frequency {} Hz)'.format(frequency1))

plt.subplot(3, 1, 2)
plt.plot(t, signal2)
plt.title('Signal 2 (Frequency {} Hz)'.format(frequency2))

plt.subplot(3, 1, 3)
# Trim the convolved_signal to match the length of convolved_t
convolved_signal = convolved_signal[:len(convolved_t)]
plt.plot(convolved_t, convolved_signal)
plt.title('Convolved Signal')
plt.xlabel('Time (s)')

plt.tight_layout()
plt.show()
