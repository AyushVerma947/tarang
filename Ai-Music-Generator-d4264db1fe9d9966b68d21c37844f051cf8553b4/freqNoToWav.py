import numpy as np
import soundfile as sf
import sounddevice as sd

duration = 5  # seconds
sampling_rate = 44100  # samples per second
frequency = 293.66  # Hz (frequency of the sine wave)
amplitude = 0.5  # Amplitude of the sine wave

t = np.linspace(0, duration, int(sampling_rate * duration), False)


def generate_sine_wave(frequency, amplitude, duration, sampling_rate):
    t = np.linspace(0, duration, int(sampling_rate * duration), False)
    sine_wave = amplitude * np.sin(2 * np.pi * frequency * t)
    return sine_wave


i = 1
while (i <= 1):
    sine_wave = generate_sine_wave(frequency, amplitude, duration, sampling_rate)
    sf.write("C:/Users/vinee/Downloads/Mini/consiqutive/freqRe.wav", sine_wave, sampling_rate)
    i = i + 1
    frequency = frequency + 1
