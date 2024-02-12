import random
import pygame
import time

# Initialize pygame mixer
pygame.mixer.init()

# Define drum sounds and their assigned probabilities
drum_sounds = {
    'kick': 0.5,    # Probability of a kick drum hit (e.g., 50%)
    'snare': 0.3,   # Probability of a snare drum hit (e.g., 30%)
    'hihat': 0.7,   # Probability of a hi-hat hit (e.g., 70%)
}

# Specify the length of the drum pattern in terms of beats or time units
num_beats = 16  # Adjust this to set the length of the drum pattern

# Generate the drum pattern based on probabilities
drum_pattern = []

for _ in range(num_beats):
    # Randomly select a drum sound based on its probability
    selected_sound = random.choices(list(drum_sounds.keys()), 
                                     weights=list(drum_sounds.values()))[0]
    
    # Add the selected drum sound to the pattern
    drum_pattern.append(selected_sound)

# Define drum sound files (you can replace these with your own sound files)
sound_files = {
    'kick': "C:\\Users\\mruna\\Downloads\\TD6K_Kick_029_73_SP.wav",
    'snare': "C:\\Users\\mruna\\Downloads\\38_SteelCup_4_SP.wav",
    'hihat': "C:\\Users\\mruna\\Downloads\\22_ClosedHat_27_138_SP.wav",
}

# Play the drum beat
for sound in drum_pattern:
    if sound in sound_files:
        pygame.mixer.Sound(sound_files[sound]).play()
    time.sleep(0.25)  # Adjust the duration between beats

# Wait for the beat to finish playing
pygame.time.wait(int(1000 * num_beats * 0.25))
