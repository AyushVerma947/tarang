import numpy as np
import matplotlib.pyplot as plt
import sounddevice as sd

# Function to convolve two signals
def convolve_signals(signal1, signal2):
    return np.convolve(signal1, signal2, 'full')

# Input from the user
num_inputs = int(input("Enter the number of frequencies to mix: "))

# Create an empty list to store the input signals
input_signals = []

# Create time-domain signals for the input frequencies
fs = 44100  # Sampling frequency (Hz)
t = np.arange(0, 1, 1/fs)  # Time values from 0 to 1 second

for i in range(num_inputs):
    frequency = float(input(f"Enter frequency {i+1} (in Hz): "))
    signal = np.sin(2 * np.pi * frequency * t)
    input_signals.append(signal)

# Initialize the convolved signal with the first input signal
convolved_signal = input_signals[0]

# Convolve all the input signals
for i in range(1, num_inputs):
    convolved_signal = convolve_signals(convolved_signal, input_signals[i])

# Normalize the convolved signal to prevent clipping
convolved_signal /= np.max(np.abs(convolved_signal))

# Play the convolved signal
print("Playing the convolved signal...")
sd.play(convolved_signal, fs)
sd.wait()
print("Playback finished.")
