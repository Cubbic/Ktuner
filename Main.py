import wx
import Layout as ly  # Layout code generated from wxGlade
import gettext # for localisation shit required by wxGlade
import aubio
import PitchDetection 




    
if __name__ == "__main__":
    gettext.install("app") 

    app = wx.App()
    
    frame = ly.MainFrame(None, wx.ID_ANY )
    #frame.derivation.SetLabel()   
    
    app.SetTopWindow(frame)
    frame.Show()
    app.MainLoop()

    input_devices_list = PitchDetection.get_input_devices()
    for i in input_devices_list :
        frame.input_list.Append(i.get('name'))
    frame.input_list.SetSelection(0)    
        
    
    
    