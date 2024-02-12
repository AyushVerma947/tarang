import pygame
import time
import numpy as np

# Initialize pygame
pygame.mixer.init()

# Frequencies for C major scale notes
scale = [261.63, 293.66, 329.63, 349.23, 392.00, 440.00, 493.88, 523.25]

def generate_wave(frequency, duration):
    sample_rate = 44100  # Standard sample rate
    t = np.linspace(0, duration, int(sample_rate * duration), False)
    wave = 0.5 * np.sin(2 * np.pi * frequency * t)
    return wave

def play_note(frequency, duration):
    wave = generate_wave(frequency, duration)
    note = pygame.mixer.Sound(buffer=wave.tobytes())  # Convert to bytes
    note.set_volume(1)  # Set volume (0 to 1)
    note.play()

def main():
    for frequency in scale:
        play_note(frequency, 0.5)  # Play each note for 0.5 seconds
        time.sleep(0.5)  # Wait for 0.5 seconds before playing the next note

if __name__ == "__main__":
    main()


    

