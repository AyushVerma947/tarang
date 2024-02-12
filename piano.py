import numpy as np
import sounddevice as sd

# Constants
A440 = 440.0
SAMPLE_RATE = 44100  # Standard audio sample rate
DURATION = 0.5      # Duration of each note in seconds
AMPLITUDE = 0.5     # Amplitude of the sine wave

# Function to generate sine wave
def generate_sine_wave(frequency, duration):
    t = np.linspace(0, duration, int(SAMPLE_RATE * duration), False)
    wave = AMPLITUDE * np.sin(2 * np.pi * frequency * t)
    return wave

# Function to play piano note
def play_piano_note(note_number):
    frequency = A440 * 2**((note_number - 49) / 12)
    wave = generate_sine_wave(frequency, DURATION)
    sd.play(wave)
    sd.wait()

# Define ranges for eight octaves (frequency bands)
octave_ranges = [
    range(21, 49),   # Sub-contra octave C0-B1
    range(49, 73),   # Contra octave C2-B3
    range(73, 97),   # Great octave C4-B5
    range(97, 121),  # Small octave C6-B7
    range(121, 145), # One-lined octave C8-B9
    range(145, 169), # Two-lined octave C10-B11
    range(169, 193), # Three-lined octave C12-B13
    range(193, 205), # Four-lined octave C14-B15
]

# Prompt the user to select an octave
print("Select an octave to play:")
for index, octave_range in enumerate(octave_ranges):
    print(f"{index+1}. Octave {index}")
selected_octave = int(input("Enter the number of the octave: "))

# Play piano notes in the selected octave range
print(f"Playing notes in Octave {selected_octave+1}")
for note_number in octave_ranges[selected_octave]:
    print(f"Playing note MIDI {note_number}")
    play_piano_note(note_number)

print("Playback complete.")
