import sounddevice as sd
import numpy as np
import time

# Define the frequencies for each note
note_freqs = { 
    'sa': 240, 
    'na': 20, 
    're': 270, 
    'ga': 300, 
    'ma': 320, 
    'pa': 360, 
    'dha': 400, 
    'ni': 450, 
}
 
# Initialize variables for the audio data 
sample_rate = 44100  # samples per second 
duration = 0.5 # in seconds 
t = np.linspace(0, duration, int(sample_rate * duration), False) 

# Define the sargam pairs 
sargam_pairs = ['sa re na re ga na ga ma na ma pa na pa dha na dha ni na ni sa'] 
 
# Specify the number of times to play the sequences 
num_iterations = 1 
 
# Play the sargam pairs in a consecutive manner for multiple iterations 
for iteration in range(num_iterations): 
    for sargam_pair in sargam_pairs: 
        notes = sargam_pair.split() 
        tones = [] 
 
        for note in notes: 
            frequency = note_freqs[note] 
            tone = 0.3 * np.sin(2 * np.pi * frequency * t) 
            tones.extend(tone) 
 
        sd.play(tones, sample_rate) 
        sd.wait()  # Wait until the sound finishes playing 
 
        time.sleep(1)  # Wait for a short interval before playing the next pair 
 
    print(f"Iteration {iteration + 1} completed.") 
 
print("All iterations completed.")