# Imports
from vosk import Model, KaldiRecognizer, SetLogLevel
SetLogLevel(-1) # The higher the more vosk logs
import pyaudio
import time
import os
os.path.dirname(os.path.abspath(__file__))

print("\nLoading...\n")

# Define the model
model = Model("Model")
framerate = 16000
rec = KaldiRecognizer(model, framerate)

# Launch the audio stream
p = pyaudio.PyAudio()
stream = p.open(format=pyaudio.paInt16, channels=1, rate=16000, input=True, frames_per_buffer=8000)
stream.start_stream()

print("\nListening...\n")

t0 = time.time()
tmax = 5 # sec, acquisition time 

while time.time() - t0 < tmax:
    # Collect the audio stream
    data = stream.read(framerate//4)
    # Process data
    rec.AcceptWaveform(data) 

# Result
print(rec.FinalResult())

# Stop the recording
stream.stop_stream()
stream.close()
p.terminate()
