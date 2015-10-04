import wx
import Layout as ly  # Layout code generated from wxGlade
import gettext # for localisation shit required by wxGlade
import aubio




    
if __name__ == "__main__":
    gettext.install("app") 

    app = wx.App()
    
    frame = ly.MainFrame(None, wx.ID_ANY )
    #frame.derivation.SetLabel()   
    
    app.SetTopWindow(frame)
    frame.Show()
    app.MainLoop()


    frame.input_list.AppendItems(["hello","hello2"])
    