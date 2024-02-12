import random

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

# Print the generated melody
print("Random Melody:", " ".join(random_melody))
