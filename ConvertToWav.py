# SEE https://github.com/jiaaro/pydub#installation
from pydub import AudioSegment
from pydub.playback import play
import wave
                                                                      
src = "Corpus/Clément 2.m4a"
dst = "Corpus/Clément 2.wav"
                                                        
sound = AudioSegment.from_file(src, format="m4a")
sound.set_channels(1) # (in mono)
sound.export(dst, format="wav")
