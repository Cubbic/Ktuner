import wx
import Layout
import gettext

ly = Layout


    
if __name__ == "__main__":
    gettext.install("app") # replace with the appropriate catalog name

    app = wx.App()
    
    frame = ly.MyFrame(None, wx.ID_ANY, "")
    app.SetTopWindow(frame)
    frame.Show()
    app.MainLoop()