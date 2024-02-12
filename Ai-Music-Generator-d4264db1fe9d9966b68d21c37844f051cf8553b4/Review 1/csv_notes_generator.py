import csv

# Define the dictionaries
A_band = {
    'Sa': 32,
    'Re': 36,
    'Ga': 41,
    'Ma': 43,
    'Pa': 48,
    'Dha': 55,
    'Ni': 61
}

B_band = {
    'Sa': 65,
    'Re': 73,
    'Ga': 82,
    'Ma': 87,
    'Pa': 98,
    'Dha': 110,
    'Ni': 123
}

C_band = {
    'Sa': 261,
    'Re': 293,
    'Ga': 329,
    'Ma': 349,
    'Pa': 392,
    'Dha': 440,
    'Ni': 493
}

D_band = {
    'Sa': 261,
    'Re': 293,
    'Ga': 329,
    'Ma': 350,
    'Pa': 392,
    'Dha':440,
    'Ni': 493
}

E_band = {
    'Sa': 329.63,
    'Re': 369.99,
    'Ga': 415.30,
    'Ma': 720,
    'Pa': 784,
    'Dha':880,
    'Ni': 987
}

F_band = {
    'Sa': 1046,
    'Re': 1174,
    'Ga': 1318,
    'Ma': 1396,
    'Pa': 1568,
    'Dha': 1760,
    'Ni': 1979
}

G_band = {
    'Sa': 2093,
    'Re': 2349,
    'Ga': 2637,
    'Ma': 2793,
    'Pa': 3136,
    'Dha': 3520,
    'Ni': 3951,
    'saa': 4186 
}

bind = {
    'A':440,
    'B':493.88,
    'C':261.63,
    'D':293.66,
    'E':329.63,
    'F':349.23,
    'G':392.0,
    'A#':466.1638,
    'Bb':466.1638, 
    'G#':415.3047,
    'Ab':415.3047,
    'F#':369.9944,
    'Gb':369.9944,
    'D#':311.1270,
    'Eb':311.1270,
    'C#':277.1826,
    'Db':277.1826,
    'gap':20
}


# Specify the CSV file name
csv_file = 'C:\Users\mruna\mini project\Review 1\notes.csv'

# Create a list of dictionaries to iterate through
bands = [A_band, B_band, C_band, D_band, E_band, F_band, G_band, bind]  # Add more dictionaries if needed

# Open the CSV file for writing
with open(csv_file, 'w', newline='') as csvfile:
    # Create a CSV writer object
    csv_writer = csv.writer(csvfile)

    # Write the header row (optional)
    csv_writer.writerow(['Band', 'Note', 'Frequency'])

    # Loop through each dictionary and write its data to the CSV file
    for band_name, band_data in zip(['A_band', 'B_band', 'C_band', 'D_band', 'E_band', 'F_band', 'G_band', 'bind'], bands):
        for note, frequency in band_data.items():
            csv_writer.writerow([band_name, note, frequency])

print(f'Data from all dictionaries has been saved to {csv_file}')
