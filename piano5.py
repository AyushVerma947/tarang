import numpy as np
import sounddevice as sd

# Define base frequencies for 'Sa' to 'Ni' in Hz (Octave -4)
base_frequencies = {
    'Sa': 16.35,
    'Re': 18.35,
    'Ga': 20.60,
    'Ma': 21.83,
    'Pa': 24.50,
    'Dha': 27.50,
    'Ni': 30.87
}

note_duration = 0.1

def generate_note_wave(frequency, duration):
    sample_rate = 44100
    t = np.linspace(0, duration, int(duration * sample_rate), False)
    envelope = np.linspace(0, 1, len(t))
    harmonics = 4
    wave = np.zeros(len(t))
    for harmonic in range(1, harmonics + 1):
        wave += (1 / harmonic) * np.sin(2 * np.pi * frequency * harmonic * t)
    wave *= envelope
    wave /= np.max(np.abs(wave))
    return wave

def play_notes_octave(pitch_shift):
    for note, base_frequency in base_frequencies.items():
        frequency = base_frequency * (2 ** pitch_shift)
        note_wave = generate_note_wave(frequency, note_duration)
        sd.play(note_wave)
        sd.wait()

if __name__ == "__main__":
    print("Playing notes of Sa Re Ga Ma Pa Dha Ni Sa across different octaves...")
    for octave_shift in range(-4, 4):  # Play in octaves -4 to 3
        play_notes_octave(octave_shift)
    print("Playback complete.")
