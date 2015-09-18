import wx

class MainWindow (wx.Frame):
    def __init__(self,parent,title):
        self.frame =  wx.Frame(None, wx.ID_ANY, "Hello World") # A Frame is a top-level window.
        self.panel = wx.Panel(self.frame, id=wx.ID_ANY,size = wx.DefaultSize)
        self.button = wx.Button(self.panel,id = wx.ID_ABOUT,label = "About man" ,pos = (10,10))
        self.frame.Show(True)





if __name__ == '__main__':
  
    app = wx.App()
    MainWindow(None, title='Size')
    app.MainLoop()