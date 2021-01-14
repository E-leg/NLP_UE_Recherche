# Imports
from vosk import Model, KaldiRecognizer, SetLogLevel
SetLogLevel(-1) # The higher the more vosk logs
import wave
import os
os.path.dirname(os.path.abspath(__file__))

print("\nLoading...\n")

# Get the audio
wf = wave.open("Audio/Clement_deb.wav")

# Get the model
model = Model("Model")
rec = KaldiRecognizer(model, wf.getframerate())

print("\nProcessing...\n")

# Process the audio
while True:
    data = wf.readframes(wf.getframerate()//4) # Get the next frames
    if len(data) == 0: 
        wf.close()
        break 

    rec.AcceptWaveform(data) # Give the frames to vosk

# Result
print(rec.FinalResult())