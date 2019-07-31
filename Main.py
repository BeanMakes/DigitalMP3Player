import wx
from CounterTimer import BackgroundTimer

count = BackgroundTimer()


class mainWindow(wx.Frame):

    def __init__(self, parent, title):
        wx.Frame.__init__(self, parent, title=title, size=(280, -1))
        self.panel = wx.Panel(self, wx.ID_ANY)
        self.CreateStatusBar()
        count.start()

        self.mainBox = self.startMenuLB()

        self.musicBox = self.listBox()

        self.musicBox.Hide()

        # Button for play
        self.buttonPl = wx.Button(self.panel, wx.ID_ANY, 'Play', (100, 100))
        self.buttonPl.Bind(wx.EVT_BUTTON, self.onPlayButton)
        self.buttonPl.Hide()

        # Button for stop
        self.buttonS = wx.Button(self.panel, wx.ID_ANY, 'Stop', (100, 150))
        self.buttonS.Bind(wx.EVT_BUTTON, self.onStopButton)
        self.buttonS.Hide()

        # Button for next
        self.buttonN = wx.Button(self.panel, wx.ID_ANY, 'Next', (190, 100))
        self.buttonN.Bind(wx.EVT_BUTTON, self.onNextButton)
        self.buttonN.Hide()

        # Button for previous
        self.buttonP = wx.Button(self.panel, wx.ID_ANY, 'Previous', (10, 100))
        self.buttonP.Bind(wx.EVT_BUTTON, self.onPrevButton)
        self.buttonP.Hide()

        self.mainBox.Bind(wx.EVT_LISTBOX_DCLICK, self.onPlayMusic)

        self.Show()

    def startMenuLB(self):
        mainMenuChoices = ["Play Music", "Create Playlist", "Edit Playlist", "Quit"]
        lb = wx.ListBox(self.panel, pos=(40, 10), size=(200, 150), choices=mainMenuChoices, style=wx.LB_SINGLE)
        return lb

    # Creating listbox for GUI
    def listBox(self):
        listBox = wx.ListBox(self.panel, pos=(40, 10), size=(200, 70), choices=count.getMusicList(), style=wx.LB_SINGLE)
        listBox.SetScrollPos(wx.HORIZONTAL, listBox.GetScrollRange(wx.HORIZONTAL), refresh=True)
        listBox.SetSelection(0)
        return listBox

    def onPlayButton(self, event):
        count.setChoice(self.musicBox.GetSelection())
        count.playMusic()

    def onStopButton(self, event):
        count.stopMusic()

    def onNextButton(self, event):
        count.nextMusic()
        self.musicBox.SetSelection(count.getChoice())

    def onPrevButton(self, event):
        count.preMusic()
        self.musicBox.SetSelection(count.getChoice())

    def onPlayMusic(self, event):
        self.mainBox.Hide()
        self.musicBox.Show()
        self.buttonPl.Show()
        self.buttonS.Show()
        self.buttonN.Show()
        self.buttonP.Show()




app = wx.App(False)
frame = mainWindow(None, "Music Player")
app.MainLoop()
count.finish()
