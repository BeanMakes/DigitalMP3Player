import MusicPlayer as mp
import wx


class mainWindow(wx.Frame):
    def __init__(self, parent, title):
        wx.Frame.__init__(self, parent, title=title, size=(200, -1))
        self.CreateStatusBar()  # A Statusbar in the bottom of the window

        panel = wx.Panel(self, wx.ID_ANY)
        button = wx.Button(panel, wx.ID_ANY, 'Play', (10, 10))
        button.Bind(wx.EVT_BUTTON, onButton)

        self.Show()


def onButton(event):
    mp.playMusic(0)


app = wx.App(False)
frame = mainWindow(None, "Hello World")


app.MainLoop()