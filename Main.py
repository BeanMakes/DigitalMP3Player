import wx
from CounterTimer import BackgroundTimer

import time

count = BackgroundTimer()
count.start()
queueMusic = []
nameSong = ""
class MainWindow(wx.Frame):

    def __init__(self, parent, title):
        wx.Frame.__init__(self, parent, title=title, size=(280, -1))
        self.InitUI()
        self.Center()
        self.Show()

    def InitUI(self):
        self.panel = wx.Panel(self, wx.ID_ANY)
        self.CreateStatusBar()
        

        self.mainBox = self.startMenuLB()


        self.mainBox.Bind(wx.EVT_LISTBOX_DCLICK, self.onPlayMusic)


    def startMenuLB(self):
        mainMenuChoices = ["Play Music", "Create Playlist", "Edit Playlist", "Quit"]
        lb = wx.ListBox(self.panel, pos=(40, 10), size=(200, 150), choices=mainMenuChoices, style=wx.LB_SINGLE)
        return lb

    def onPlayMusic(self, event):
        self.Close()
        SelectMusicWindow(None, "Music Player")


class SelectMusicWindow(wx.Frame):

    def __init__(self, parent, title):
        wx.Frame.__init__(self, parent, title=title, size=(280, -1))
        self.InitUI() 
        self.Centre() 
        self.Show()
    
    def InitUI(self):
        self.p = wx.Panel(self) 
        vbox = wx.BoxSizer(wx.VERTICAL) 

        self.musicBox = self.listBox()

        vbox.Add(self.musicBox,0,  wx.EXPAND, 20)

        vbox.AddStretchSpacer(1) 

        hbox = wx.BoxSizer(wx.HORIZONTAL) 

        btnBack = wx.Button(self.p,label="Back")
        btnBack.Bind(wx.EVT_BUTTON, self.onBackButton)
        hbox.Add(btnBack,0, wx.ALIGN_CENTER )

        hbox.AddStretchSpacer(1)  

        self.btnPlay = wx.Button(self.p,label="Play")
        self.btnPlay.Bind(wx.EVT_BUTTON, self.onPlayButton)
        hbox.Add(self.btnPlay,0, wx.ALIGN_CENTER )

        vbox.Add(hbox,1,wx.ALL|wx.EXPAND) 

        self.p.SetSizer(vbox) 

    def listBox(self):
        listBox = wx.ListBox(self.p, pos=(40, 10), size=(200, 70), choices=count.getMusicList(), style=wx.LB_SINGLE)
        listBox.SetScrollPos(wx.HORIZONTAL, listBox.GetScrollRange(wx.HORIZONTAL), refresh=True)
        listBox.SetSelection(0)
        return listBox
    
    def onPlayButton(self, event):
        self.Close()
        count.setChoice(self.musicBox.GetSelection())
        count.playMusic()
        frame = PlayMusicWindow(None, "Music Player")

    def onBackButton(self, event):
        count.stopMusic()
        self.Close()
        frame = MainWindow(None, "Music Player")

class PlayMusicWindow(wx.Frame):
    def __init__(self, parent, title):
        wx.Frame.__init__(self, parent, title=title, size=(280, 450))
        self.InitUI() 
        self.Centre() 
        self.Show()
        self.playing = True

    def InitUI(self):
        p = wx.Panel(self) 
        vbox = wx.BoxSizer(wx.VERTICAL) 
        self.l1 = wx.StaticText(p,label = count.getMusicName(),style = wx.ALIGN_CENTRE ) 
        vbox.AddStretchSpacer(1) 
        vbox.Add(self.l1,0,  wx.EXPAND, 20) 
        vbox.AddStretchSpacer(1) 

        img_path = "Images/images.jpg"
        img = wx.Image(img_path, wx.BITMAP_TYPE_ANY)
        img = img.Scale(200,150)
        self.imageCtrl = wx.StaticBitmap(p, wx.ID_ANY,wx.BitmapFromImage(img))

        vbox.Add(self.imageCtrl, 0, wx.ALIGN_CENTER) 

        self.sld = wx.Slider(p, value = 10, minValue = 1, maxValue = 100, style = wx.SL_HORIZONTAL|wx.SL_LABELS,size=(200,20))
        vbox.Add(self.sld,1,flag = wx.ALIGN_CENTER_HORIZONTAL | wx.TOP, border = 20)  
        hbox = wx.BoxSizer(wx.HORIZONTAL) 

        bmp = wx.Bitmap('Images/PrevButton.png') 
        b3 = wx.Button(p)
        b3.Bind(wx.EVT_BUTTON, self.onPrevButton)
        b3.SetBitmap(bmp) 
        hbox.Add(b3,0, wx.ALIGN_CENTER ) 

        bmp = wx.Bitmap('Images/PlayButton.png') 

        b4 = wx.Button(p) 
        b4.Bind(wx.EVT_BUTTON, self.onPlayButton)
        b4.SetBitmap(bmp) 

        hbox.AddStretchSpacer(1) 
        hbox.Add(b4,0,wx.ALIGN_CENTER ) 
        hbox.AddStretchSpacer(1) 

        bmp = wx.Bitmap('Images/NextButton.png') 
        b5 = wx.Button(p)
        b5.Bind(wx.EVT_BUTTON, self.onNextButton)
        b5.SetBitmap(bmp) 

        hbox.Add(b5,0,wx.ALIGN_CENTER ) 
        vbox.Add(hbox,1,wx.ALL|wx.EXPAND) 
        b6 = wx.Button(p,label = "Back") 
        b6.Bind(wx.EVT_BUTTON, self.onBackButton)
        vbox.Add(b6,0,wx.ALIGN_CENTER) 
        p.SetSizer(vbox) 

    def onBackButton(self, event):
        count.stopMusic()
        self.Close()
        frame = SelectMusicWindow(None, "Music Player")

    def onNextButton(self, event):
        count.nextMusic()
        self.l1.SetLabel(count.getMusicName())

    def onPrevButton(self, event):
        count.preMusic()
        self.l1.SetLabel(count.getMusicName())

    def onPlayButton(self, event):
        if self.playing:
            count.stopMusic()
            self.playing=False
        else:
            count.playMusic()
            self.playing=True

app = wx.App(False)
frame = MainWindow(None, "Music Player")
app.MainLoop()
count.finish()
