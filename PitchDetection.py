import analyse #soundanalyse
import Layout as ly
import numpy
import alsaaudio 
import threading


def get_input_devices ():
        return alsaaudio.pcms(alsaaudio.PCM_CAPTURE)
        
def start_stream ():
        inp = alsaaudio.PCM(type= alsaaudio.PCM_CAPTURE, mode=alsaaudio.PCM_NORMAL,device='default')
        inp.setchannels(1)
        inp.setrate(44100)
        inp.setformat(alsaaudio.PCM_FORMAT_S16_LE)
        inp.setperiodsize(1024)
        while True:
                length, data = inp.read()
                samps = numpy.fromstring(data, dtype='int16')                
                #print analyse.musical_detect_pitch(samps)      

detect_pitch_thread = threading.Thread(target=start_stream)
detect_pitch_thread.start()


