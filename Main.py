from MusicPlayer import MusicPlayer
import wx


mp = MusicPlayer()


class mainWindow(wx.Frame):

    def __init__(self, parent, title):
        wx.Frame.__init__(self, parent, title=title, size=(200, -1))
        self.CreateStatusBar()  # A Statusbar in the bottom of the window

        panel = wx.Panel(self, wx.ID_ANY)
        button = wx.Button(panel, wx.ID_ANY, 'Play', (10, 10))
        button.Bind(wx.EVT_BUTTON, onPlayButton)

        buttonS = wx.Button(panel, wx.ID_ANY, 'Stop', (10, 50))
        buttonS.Bind(wx.EVT_BUTTON, onStopButton)

        self.Show()


def onPlayButton(event):
    mp.checkMusic()
    mp.setChoice = 0
    mp.playMusic()


def onStopButton(event):
    mp.stopMusic()


app = wx.App(False)
frame = mainWindow(None, "Music Player")


app.MainLoop()