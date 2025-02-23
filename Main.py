import wx
from CounterTimer import BackgroundTimer

import time

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

        # Progressbar 
        self.gauge = wx.Gauge(self.panel, range = 20, pos = (40, 200),size = (100,20), style =wx.GA_HORIZONTAL)
        self.gauge.Hide()

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
        print(count.getSongLength())
        self.gauge.SetRange(count.getSongLength())
        self.gauge.SetValue(count.getSongLength())

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
        self.gauge.Show()


class playMusicWindow(wx.Frame):
    def __init__(self, parent, title):
        wx.Frame.__init__(self, parent, title=title, size=(280, 450))
        self.InitUI() 
        self.Centre() 
        self.Show()

    def InitUI(self):
        p = wx.Panel(self) 
        vbox = wx.BoxSizer(wx.VERTICAL) 
        l1 = wx.StaticText(p,label = "Title of Song",style = wx.ALIGN_CENTRE ) 
        vbox.AddStretchSpacer(1) 
        vbox.Add(l1,0,  wx.EXPAND, 20) 
        vbox.AddStretchSpacer(1) 
        # b1 = wx.Button(p, label = "Btn1") 
        # vbox.Add(b1,0,wx.EXPAND) 
        
        # img = wx.EmptyImage(100,100)

        img_path = "Images/images.jpg"
        img = wx.Image(img_path, wx.BITMAP_TYPE_ANY)
        img = img.Scale(200,150)
        self.imageCtrl = wx.StaticBitmap(p, wx.ID_ANY,wx.BitmapFromImage(img))
        # png = wx.Image(img_path, wx.BITMAP_TYPE_ANY)
        # image.SetBitmap(wx.Bitmap(img_path))

        # b2 = wx.Button(p, label = "Btn2") 
        vbox.Add(self.imageCtrl, 0, wx.ALIGN_CENTER) 
        # t = wx.TextCtrl(p) 
        self.sld = wx.Slider(p, value = 10, minValue = 1, maxValue = 100, style = wx.SL_HORIZONTAL|wx.SL_LABELS,size=(200,20))
        vbox.Add(self.sld,1,flag = wx.ALIGN_CENTER_HORIZONTAL | wx.TOP, border = 20)  
        hbox = wx.BoxSizer(wx.HORIZONTAL) 
        # l2 = wx.StaticText(p,label = "Label2", style = wx.ALIGN_CENTRE) 
        bmp = wx.Bitmap('Images/PrevButton.png') 
        b3 = wx.Button(p)
        b3.SetBitmap(bmp) 
        hbox.Add(b3,0, wx.ALIGN_CENTER ) 

        bmp = wx.Bitmap('Images/PlayButton.png') 

        b4 = wx.Button(p) 
        b4.SetBitmap(bmp) 

        hbox.AddStretchSpacer(1) 
        hbox.Add(b4,0,wx.ALIGN_CENTER ) 
        hbox.AddStretchSpacer(1) 

        bmp = wx.Bitmap('Images/NextButton.png') 
        b5 = wx.Button(p)
        b5.SetBitmap(bmp) 

        hbox.Add(b5,0,wx.ALIGN_CENTER ) 
        vbox.Add(hbox,1,wx.ALL|wx.EXPAND) 
        b6 = wx.Button(p,label = "Btn6") 
        vbox.Add(b6,0,wx.ALIGN_CENTER) 
        p.SetSizer(vbox) 

app = wx.App(False)
frame = playMusicWindow(None, "Music Player")
app.MainLoop()
count.finish()
