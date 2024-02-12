import numpy as np
import sounddevice as sd

# Define the frequency of 'Sa' (C) note in Hz
sa_base_frequency = 261.63  # 'Sa' note in octave 4 (C4)

# Define the duration of each note in seconds
note_duration = 0.5

# Function to generate a sine wave with amplitude envelope and harmonics
def generate_note_wave(frequency, duration):
    sample_rate = 44100
    t = np.linspace(0, duration, int(duration * sample_rate), False)
    
    # Create an amplitude envelope (ramp up and down)
    envelope = np.linspace(0, 1, len(t))
    
    # Generate harmonics by adding multiple sine waves
    harmonics = 4
    wave = np.zeros(len(t))
    for harmonic in range(1, harmonics + 1):
        wave += (1 / harmonic) * np.sin(2 * np.pi * frequency * harmonic * t)
    
    # Apply amplitude envelope
    wave *= envelope
    
    # Normalize the wave to prevent clipping
    wave /= np.max(np.abs(wave))
    
    return wave

# Play 'Sa' note of different octaves by changing pitch
def play_sa_octave(pitch_shift):
    sa_frequency = sa_base_frequency * (2 ** pitch_shift)
    note_wave = generate_note_wave(sa_frequency, note_duration)
    sd.play(note_wave)
    sd.wait()

if __name__ == "__main__":
    print("Playing 'Sa' note of different octaves by changing pitch...")
    for octave_shift in range(-4, 4):  # Play in octaves -4 to 3 from the base frequency
        play_sa_octave(octave_shift)
    print("Playback complete.")
