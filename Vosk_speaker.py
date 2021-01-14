# Imports
from vosk import Model, KaldiRecognizer, SpkModel, SetLogLevel
SetLogLevel(-1) # The higher the more vosk logs
import numpy as np
import wave
import json
import os
os.path.dirname(os.path.abspath(__file__))

print("\nLoading...\n")

# Get an audio with a speaker utterance
wf = wave.open("Audio/Clement_utterance.wav")
# Utterance should be at least longer than 4 seconds to give reliable xvector

# Get the models
model = Model("Model")
spk_model = SpkModel("ModelSpk/vosk-model-spk-0.4")
rec = KaldiRecognizer(model, spk_model, wf.getframerate())

# Reference speaker X-vector (for vosk-model-spk-0.4)
ref_spk = [7.503349, 3.43545, 3.454909, 2.563787, 2.663408, 5.062055, 4.764707, 4.449105, 3.541641, -1.050396, 3.720739, 2.640637, 5.103586, 1.256302, -3.173411, 0.082178, 2.944211, 5.246361, -0.677061, 4.025254, -1.063051, 0.649299, 5.65843, 4.593107, 2.438464, -0.230208, 4.884412, 3.195941, 4.726738, 8.070119, 5.769555, -1.215657, 0.883402, 7.316496, 1.687734, -0.562641, 2.429686, -3.074908, 5.532275, 6.355387, 5.17332, 2.072405, 1.088864, 3.405548, 2.655332, -1.562446, -3.529907, 7.393252, 4.068328, 4.117475, 5.473275, 5.278838, 0.654979, 4.88297, -2.98639, 0.84448, 6.115485, -0.431109, 0.040032, 3.956203, -1.855702, -1.134009, 3.872649, 1.256854, 0.868025, 5.501782, 3.180627, 0.994407, -1.615914, 6.528112, 6.594543, 0.307433, 4.281507, -0.481726, 3.292697, 1.677757, 2.487656, 4.781837, 4.603899, 5.156174, 7.718985, 1.683772, 1.690143, 2.294749, 2.206486, -5.641241, 1.801123, -1.340744, 3.359111, 7.558606, 0.896842, 5.844481, -0.511804, 5.016039, 3.829097, 1.397049, 4.272022, -0.844127, 5.277065, 1.431148, 0.297183, 4.613814, 1.780515, 4.217468, 2.079824, 4.387954, 0.429339, 2.788964, -4.339468, 7.726006, 2.821522, 0.686194, 4.850358, -0.231629, 6.031162, 2.970448, 4.464263, 3.749392, 8.132429, 4.02894, -0.339672, 8.399939, 0.932482, 1.085174, 2.968254, -2.172826, 4.337935, -1.468485]

# Distance used between X-vectors
def cosine_dist(x, y):
    nx = np.array(x)
    ny = np.array(y)
    return 1 - np.dot(nx, ny) / np.linalg.norm(nx) / np.linalg.norm(ny)

print("\nProcessing...\n")

# Process the audio
while True:
    data = wf.readframes(wf.getframerate()//4) # Get the next frames
    if len(data) == 0:
        wf.close()
        break

    rec.AcceptWaveform(data) # Give the frames to vosk

# Results
res = json.loads(rec.FinalResult())
print ("\nText:", res['text'], "\n")
print ("Speaker distance:", cosine_dist(ref_spk, res['spk']), "\n") # Comparison to the reference speaker
print ("X-vector:", res['spk']) # Fingerprint of the speaker
