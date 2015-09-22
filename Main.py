import wx
import Layout  # Layout code generated from wxGlade
import gettext # for localisation shit required by wxGlade
import aubio

ly = Layout



    
if __name__ == "__main__":
    gettext.install("app") 

    app = wx.App()
    
    frame = ly.MainFrame(None, wx.ID_ANY )
    #frame.derivation.SetLabel()   
    
    app.SetTopWindow(frame)
    frame.Show()
    app.MainLoop()



        