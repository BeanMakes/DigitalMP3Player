from MusicPlayer import MusicPlayer
import wx
import time
from CounterTimer import SecondCounter

mp = MusicPlayer()


class mainWindow(wx.Frame):

    def __init__(self, parent, title):
        wx.Frame.__init__(self, parent, title=title, size=(280, -1))
        self.CreateStatusBar()  # A Statusbar in the bottom of the window
        count = SecondCounter()
        count.start()

        panel = wx.Panel(self, wx.ID_ANY)

        # Creating listbox for GUI
        def listBox(self):
            self.text = wx.TextCtrl(panel, style=wx.TE_MULTILINE)
            listBox = wx.ListBox(panel, pos=(40, 10), size=(200, 70), choices=mp.getMusicList(), style=wx.LB_SINGLE)
            listBox.SetScrollPos(wx.HORIZONTAL, listBox.GetScrollRange(wx.HORIZONTAL), refresh=True)
            listBox.SetSelection(0)
            return listBox

        musicBox = listBox(self)

        def onPlayButton(event):
            mp.setChoice(musicBox.GetSelection())
            mp.playMusic()

        def onStopButton(event):
            mp.stopMusic()
            print(count.finish())

        def onNextButton(event):
            mp.nextMusic()
            musicBox.SetSelection(mp.getChoice())

        def onPrevButton(event):
            mp.preMusic()
            musicBox.SetSelection(mp.getChoice())

        #Button for play
        button = wx.Button(panel, wx.ID_ANY, 'Play', (100, 100))
        button.Bind(wx.EVT_BUTTON, onPlayButton)

        #Button for stop
        buttonS = wx.Button(panel, wx.ID_ANY, 'Stop', (100, 150))
        buttonS.Bind(wx.EVT_BUTTON, onStopButton)

        #Button for next
        buttonN = wx.Button(panel, wx.ID_ANY, 'Next', (190, 100))
        buttonN.Bind(wx.EVT_BUTTON, onNextButton)

        #Button for previous
        buttonP = wx.Button(panel, wx.ID_ANY, 'Previous', (10, 100))
        buttonP.Bind(wx.EVT_BUTTON, onPrevButton)

        self.Show()


def loop1_10():
    for i in range(1, 11):
        time.sleep(1)
        print(i)


#threading.Thread(target=loop1_10).start()

mp.checkMusic()
app = wx.App(False)
frame = mainWindow(None, "Music Player")
app.MainLoop()
