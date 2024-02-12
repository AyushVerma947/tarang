import numpy as np
import sounddevice as sd

# Function to generate a sinusoidal waveform for a given frequency and duration
def generate_sine_wave(frequency, duration, sample_rate):
    t = np.linspace(0, duration, int(sample_rate * duration), endpoint=False)
    return 0.5 * np.sin(2 * np.pi * frequency * t)

# Input from the user
num_inputs = int(input("Enter the number of frequencies to mix: "))

# Set the duration and sample rate for the audio
duration = 3  # seconds
sample_rate = 44100  # samples per second

# Initialize the mixed signal with zeros
mixed_signal = np.zeros(int(duration * sample_rate))

# Generate and mix sine waves for each frequency
for i in range(num_inputs):
    frequency = float(input(f"Enter frequency {i + 1} (in Hz): "))
    sine_wave = generate_sine_wave(frequency, duration, sample_rate)
    mixed_signal += sine_wave

# Normalize the mixed signal to prevent clipping
mixed_signal /= np.max(np.abs(mixed_signal))

# Play all the frequencies simultaneously
sd.play(mixed_signal, sample_rate)
sd.wait()
print('played.')
