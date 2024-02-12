import numpy as np
import soundfile as sf

# Parameters
duration = 5  # seconds
sampling_rate = 44100  # samples per second
frequency = 20  # Hz (frequency of the sine wave)
amplitude = 0.5  # Amplitude of the sine wave

# Generate time values
t = np.linspace(0, duration, int(sampling_rate * duration), False)

# Generate the sine wave
sine_wave = amplitude * np.sin(2 * np.pi * frequency * t)

# Save the audio to a file
i=1000
while(i<=1000):
    sf.write("C:/Users/mruna/mini project/Review 1/frequency_DataSet/freq{}.wav".format(i), sine_wave, sampling_rate)
    i=i+1
    frequency = 9000

import numpy as np
import sounddevice as sd

def generate_sine_wave(frequency, amplitude, duration, sampling_rate):
    t = np.linspace(0, duration, int(sampling_rate * duration), False)
    sine_wave = amplitude * np.sin(2 * np.pi * frequency * t)
    return sine_wave

# Parameters
frequency = 20     # A4 (440 Hz) - change to desired frequency
amplitude = 0.5  # Change to desired amplitude (0.0 to 1.0)
duration = 5     # Change to desired duration in seconds
sampling_rate = 44100  # Common sampling rate for audio

# Generate sine wave
sine_wave = generate_sine_wave(frequency, amplitude, duration, sampling_rate)

# Play the generated sound
sd.play(sine_wave, sampling_rate)
sd.wait()