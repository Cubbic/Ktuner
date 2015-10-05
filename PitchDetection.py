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
        
get_input_devices()