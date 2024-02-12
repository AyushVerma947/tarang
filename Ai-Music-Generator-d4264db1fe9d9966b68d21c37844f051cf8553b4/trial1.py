import pygame
import os

# Initialize pygame
pygame.init()

def play_audio(file_path):
    # Initialize the mixer module for audio
    pygame.mixer.init()

    # Load the audio file
    sound = pygame.mixer.Sound(file_path)

    # Play the audio
    sound.play()

# Replace 'your_audio_file.wav' with your actual audio file's path
audio_file_path = "C:/Users/mruna/mini project/sa re ga/freqSa.wav"

# Check if the file exists
if os.path.exists(audio_file_path):
    play_audio(audio_file_path)
else:
    print("Audio file not found.")
