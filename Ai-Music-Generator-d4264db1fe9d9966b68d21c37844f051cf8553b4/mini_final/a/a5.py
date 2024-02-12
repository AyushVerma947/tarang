import random
import pygame
import time
import numpy as np

# Initialize pygame mixer
pygame.mixer.init()

# Define the musical scale (C major scale in this example)
scale = ['C', 'D', 'E', 'F', 'G', 'A', 'B']

# Define the length of the melody (number of notes)
melody_length = 10  # You can adjust this to your desired length

# Generate a random melody
random_melody = []

for _ in range(melody_length):
    # Randomly select a note from the scale
    random_note = random.choice(scale)
    random_melody.append(random_note)

# Print and play the generated melody
print("Random Melody:", " ".join(random_melody))

# Define a dictionary to map note names to their frequencies
note_freqs = {
    'C': 261.63,
    'D': 293.66,
    'E': 329.63,
    'F': 349.23,
    'G': 392.00,
    'A': 440.00,
    'B': 493.88,
}

# Create a custom waveform for each note frequency
note_waveforms = {}
sample_rate = 44100  # Adjust the sample rate as needed

for note, frequency in note_freqs.items():
    t = np.linspace(0, 0.5, int(sample_rate * 0.5), False)  # 0.5 seconds duration
    wave = 0.5 * np.sin(2 * np.pi * frequency * t)
    note_waveforms[note] = wave

# Play the melody
for note in random_melody:
    wave = note_waveforms.get(note)
    if wave is not None:
        sound = pygame.mixer.Sound(wave.astype(np.float32))
        sound.play()
        time.sleep(0.5)  # Adjust the duration between notes

# Wait for the melody to finish playing
pygame.time.wait(int(1000 * melody_length * 0.5))
