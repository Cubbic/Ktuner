import pyaudio
import analyse #soundanalyse
import Layout as ly
import numpy


p = pyaudio.PyAudio()
def get_input_devices ():
        
        info = p.get_host_api_info_by_index(0)
        
        numdevices = info.get('deviceCount')
        
        input_devices_list = []
        #for each audio device, determine if is an input or an output and add it to the appropriate list and dictionary
        for i in range (0,numdevices):
                if p.get_device_info_by_host_api_device_index(0,i).get('maxInputChannels')>0:
                        #print "Input Device id ", i, " - ", p.get_device_info_by_host_api_device_index(0,i).get('name')
                        input_devices_list.append ( p.get_device_info_by_host_api_device_index(0,i) )
                     
          
        p.terminate()
        return input_devices_list
        
def start_stream ():
        stream = p.open(
                format = pyaudio.paInt16,
                channels = 1,
                rate = int(p.get_device_info_by_index(1)['defaultSampleRate']),
                input_device_index = 1,
                input = True)
        print int(p.get_device_info_by_index(1)['defaultSampleRate'])
        while True:
                # Read raw microphone data
                rawsamps = stream.read(1024)
                # Convert raw data to NumPy array
                samps = numpy.fromstring(rawsamps, dtype=numpy.int16)
                # Show the volume and pitch
                print analyse.loudness(samps), analyse.musical_detect_pitch(samps)
                
start_stream()                
        