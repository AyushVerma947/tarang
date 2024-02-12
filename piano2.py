import numpy as np
import sounddevice as sd
import time


# Define note frequencies


A_band = {
    'Sa': 32,
    'Re': 36,
    'Ga': 41,
    'Ma': 43,
    'Pa': 48,
    'Dha': 55,
    'Ni': 61
}

B_band = {
    'Sa': 65,
    'Re': 73,
    'Ga': 82,
    'Ma': 87,
    'Pa': 98,
    'Dha': 110,
    'Ni': 123
}

C_band = {
    'Sa': 261.63,
    'Re': 293.66,
    'Ga': 329.63,
    'Ma': 349.23,
    'Pa': 392.00,
    'Dha':440.00,
    'Ni': 493.88
}

D_band = {
    'Sa': 261,
    'Re': 293,
    'Ga': 329,
    'Ma': 350,
    'Pa': 392,
    'Dha':440,
    'Ni': 493
}

E_band = {
    'Sa': 329.63,
    'Re': 369.99,
    'Ga': 415.30,
    'Ma': 720,
    'Pa': 784,
    'Dha':880,
    'Ni': 987
}

F_band = {
    'Sa': 1046,
    'Re': 1174,
    'Ga': 1318,
    'Ma': 1396,
    'Pa': 1568,
    'Dha': 1760,
    'Ni': 1979
}

G_band = {
    'Sa': 2093,
    'Re': 2349,
    'Ga': 2637,
    'Ma': 2793,
    'Pa': 3136,
    'Dha': 3520,
    'Ni': 3951,
    'saa': 4186 
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
    frequency = C_band[note]
    note_wave = generate_note_wave(frequency, note_duration)
    sd.play(note_wave)
    sd.wait()

# Ensure all sounds are played before the program exits
sd.stop()
