import numpy as np
import sounddevice as sd

# Function to generate a sinusoidal waveform for a given frequency and duration
def generate_sine_wave(frequency, duration, sample_rate):
    t = np.linspace(0, duration, int(sample_rate * duration), endpoint=False)
    return 0.5 * np.sin(2 * np.pi * frequency * t)

# Take user input for the two frequencies
frequency1 = float(input("Enter the first frequency (in Hz): "))
frequency2 = float(input("Enter the second frequency (in Hz): "))

# Set the duration and sample rate for the audio
duration = 3  # seconds
sample_rate = 44100  # samples per second

# Generate sine waves for the two frequencies
sine_wave1 = generate_sine_wave(frequency1, duration, sample_rate)
sine_wave2 = generate_sine_wave(frequency2, duration, sample_rate)

# Mix the two signals by adding them together
mixed_signal = sine_wave1 + sine_wave2

# Normalize the mixed signal to prevent clipping
mixed_signal /= np.max(np.abs(mixed_signal))

# Play the mixed signal
sd.play(mixed_signal, sample_rate)
sd.wait()
print('played.')