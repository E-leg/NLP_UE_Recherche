import deepspeech
from deepspeech import Model
import wave
import numpy as np

# On charge le model
model = Model("deepspeech-0.9.1-models.pbmm")

# On charge l'audio au format 16 kHz
wf = wave.open("obama_mono_16.wav")
frames = wf.getnframes()
buffer = wf.readframes(frames)

# On convertit les bytes en array
data16 = np.frombuffer(buffer, dtype=np.int16)

model.stt(data16)

"""
Output :
"it is bot fundamental belief i am my brother's keeper i am my fisters keeper that makes this country work it's what a lows us to pursue our individual dreams and yet sill come together as one american family he por this ownim out of many one now even as we speak they are those who are preparing to divide us the spin masters the negave ad hadlers who ambrace the politics of anything goes well i say to them to night there is not a liberal america and a conservative america there is be united states of america veri is not a blac omerica and a write america and latino america and asian america thers the united states of tamerica the punnance the penens like the slice an ti ar country in the red stace and blu states red state for republicans lose state for democrats but out gun news for them to we were ship en us of god in the blue face and we don like petera lagence pokin around in our libraries in the red stace we con wetole and the blue face and yes we' got some gay frinds in the web states ter a tank ra o pols the lorin a rock and their picrich os supported the war in a rock we are one people all lov us pledging a legiance to the stars and strikes oh a bu's tefending that younited states of america"
"""