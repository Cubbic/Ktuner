import pyaudio
import analyse #soundanalyse
import Layout as ly
import numpy,time
import alsaaudio ,wave


def get_input_devices ():
        pass
        
def start_stream ():
        inp = alsaaudio.PCM(type= alsaaudio.PCM_CAPTURE, mode=alsaaudio.PCM_NORMAL,device='default')
        inp.setchannels(1)
        inp.setrate(44100)
        inp.setformat(alsaaudio.PCM_FORMAT_S16_LE)
        inp.setperiodsize(1024)
        while True:
                length, data = inp.read()
                samps = numpy.fromstring(data, dtype='int16')                
                print analyse.musical_detect_pitch(samps)      
start_stream()                
        