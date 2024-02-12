import csv
import numpy as np
import sounddevice as sd

# Define the duration of each note in seconds
note_duration = 0.5

# Function to generate a sine wave for a given frequency and duration
def generate_note_wave(frequency, duration):
    t = np.linspace(0, duration, int(duration * 44100), False)
    wave = 0.5 * np.sin(2 * np.pi * frequency * t)
    return wave

# Specify the dictionary you want to use (e.g., 'C_band')
selected_band = 'C_band'

# Read note frequencies from the "notes.csv" file for the selected dictionary
note_frequencies = {}

with open('notes.csv', 'r') as csvfile:
    csv_reader = csv.reader(csvfile)
    next(csv_reader)  # Skip the header row if it exists
    for row in csv_reader:
        band, note, frequency = row
        if band == selected_band:
            note_frequencies[note] = float(frequency)

# Create a simple melody using the note frequencies from the selected dictionary
melody = ['Sa', 'Re', 'Ga', 'Ma', 'Pa', 'Dha', 'Ni']

# Generate and play the melody
for note in melody:
    frequency = note_frequencies.get(note, 0)  # Default to 0 if note not found
    note_wave = generate_note_wave(frequency, note_duration)
    sd.play(note_wave)
    sd.wait()

# Ensure all sounds are played before the program exits
sd.stop()
