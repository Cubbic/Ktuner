import pyaudio
import aubio
import Layout as ly

def get_input_devices ():
        p = pyaudio.PyAudio()
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
        FORMAT = pyaudio.paInt16
        CHANNELS = 2
        RATE = 44100
        CHUNK = 1024
        RECORD_SECONDS = 5
        
        
        audio = pyaudio.PyAudio()
             
        # start Recording
        stream = audio.open(format=FORMAT, channels=CHANNELS,rate=RATE, input=True,frames_per_buffer=CHUNK,
                            input_device_index = None
        print "recording..."
        frames = []
        
        for i in range(0, int(RATE / CHUNK * RECORD_SECONDS)):
                data = stream.read(CHUNK)
                frames.append(data)
        print "finished recording"
        
        
        # stop Recording
        stream.stop_stream()
        stream.close()
        audio.terminate()
                
start_stream()                
        