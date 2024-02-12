import pygame
import time

# Initialize pygame mixer
pygame.mixer.init()

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

# Play the melody
for note, duration in melody:
    if note == 'rest':
        time.sleep(duration)  # Rest
    else:
        frequency = note_freqs.get(note, 0)
        if frequency > 0:
            pygame.mixer.Sound(frequency).play()
            time.sleep(duration)

# Wait for the melody to finish playing
pygame.time.wait(int(1000 * sum(duration for _, duration in melody)))
