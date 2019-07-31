import threading
import time
from MusicPlayer import MusicPlayer

mp = MusicPlayer()

class BackgroundTimer(threading.Thread):

    # create a thread object that will do the counting in the background

    def __init__(self, interval=1):
        # init the thread
        threading.Thread.__init__(self)
        self.__interval = interval  # seconds
        # initial value
        self.__value = 0
        # controls the while loop in method run
        self.__alive = False
        # Sets time for end of song
        self.__endOfSong = 0
        mp.checkMusic()

    def run(self):
        # this will run in its own thread via self.start()
        self.__alive = True
        while self.__alive:
            time.sleep(self.__interval)
            # update count value
            self.__value += self.__interval
            print(self.__value)
            if self.__endOfSong != 0:
                # When song is finished play next song
                if self.__endOfSong <= self.__value:
                    print("Finished song")
                    self.__nextMusic()

    def peek(self):
        # return the current value
        return self.__value

    def finish(self):
        # close the thread, return final value
        # stop the while loop in method run
        self.__alive = False
        return self.__value

    # All methods used in MusicPlayer rewritten here to use for GUI

    def playMusic(self):
        mp.playMusic()
        # Sets the time the song wll end
        self.__endOfSong = self.__value + (mp.getSize()/44190)

    def stopMusic(self):
        # Sets the time the song wll end
        self.__endOfSong = 0
        mp.stopMusic()

    def nextMusic(self):
        mp.nextMusic()
        # Sets the time the song wll end
        self.__endOfSong = self.__value + (mp.getSize()/44190)

    def preMusic(self):
        mp.preMusic()
        # Sets the time the song wll end
        self.__endOfSong = self.__value + (mp.getSize()/44190)

    def setChoice(self,choice):
        mp.setChoice(choice)

    def getChoice(self):
        return mp.getChoice()

    def getMusicList(self):
        return mp.getMusicList()

