import numpy as np
import sounddevice as sd
import time

# Define note frequencies
note_frequencies = {
    'Sa': 240,
    'Re': 270,
    'Ga': 300,
    'Ma': 320,
    'Pa': 360,
    'Dha': 400,
    'Ni': 450
}

# Define the duration of each note in seconds
note_duration = 0.5

# Function to generate a sine wave for a given frequency and duration
def generate_note_wave(frequency, duration):
    t = np.linspace(0, duration, int(duration * 44100), False)
    wave = 0.5 * np.sin(2 * np.pi * frequency * t)
    return wave

# Create a simple melody using the note frequencies
melody = ['Sa', 'Re', 'Ga', 'Ma', 'Pa', 'Dha', 'Ni']

# Generate and play the melody
for note in melody:
    frequency = note_frequencies[note]
    note_wave = generate_note_wave(frequency, note_duration)
    sd.play(note_wave)
    sd.wait()

# Ensure all sounds are played before the program exits
sd.stop()
