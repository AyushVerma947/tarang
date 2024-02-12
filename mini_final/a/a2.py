import random

# Define possible note durations and their corresponding beats
note_durations = {
    'quarter': 1.0,
    'eighth': 0.5,
    'rest': 0.0,  # Represents a rest (no sound)
}

# Define the time signature and the number of beats per measure
time_signature = (4, 4)  # 4/4 time signature (4 beats per measure)

# Specify the length of the melody in terms of the number of measures
num_measures = 4

# Define a set of fixed notes that you want to use in the melody
fixed_notes = ['C', 'D', 'E', 'F', 'G', 'A', 'B']

# Generate and combine random rhythms with fixed notes to create the melody
melody = []

for _ in range(num_measures):
    measure_length = time_signature[0]  # Number of beats in the measure
    measure = []

    while measure_length > 0:
        # Randomly select a note duration or rest
        random_duration = random.choice(list(note_durations.keys()))
        duration_in_beats = note_durations[random_duration]

        # Check if the selected duration fits within the remaining beats in the measure
        if duration_in_beats <= measure_length:
            if random_duration != 'rest':
                # If it's not a rest, randomly select a note from the fixed set
                random_note = random.choice(fixed_notes)
                measure.append((random_note, random_duration))
            else:
                measure.append(('rest', random_duration))
            
            measure_length -= duration_in_beats

    melody.extend(measure)

# Print the generated melody
for note, duration in melody:
    if note == 'rest':
        print(f"Rest ({duration} beats)")
    else:
        print(f"Note {note} ({duration} beats)")

