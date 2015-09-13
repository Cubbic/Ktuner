import wx

app = wx.App(False)  # Create a new app, don't redirect stdout/stderr to a window.
frame = wx.Frame(None, wx.ID_ANY, "Hello World") # A Frame is a top-level window.
frame.Show(True)     # Show the frame.

panel = wx.Panel(frame, id=wx.ID_ANY)
button = wx.Button(panel,id = wx.ID_ABOUT,label = "About man")
panel.Show()
button.Show()


app.MainLoop()
