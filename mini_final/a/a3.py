import random

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

# Print the generated drum pattern
for beat, sound in enumerate(drum_pattern, start=1):
    print(f"Beat {beat}: {sound}")
