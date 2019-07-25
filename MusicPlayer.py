import os
import simpleaudio as sa


class MusicPlayer:
    def __init__(self):
        self.__musicList = []
        self.__musicDirectory = './Music/'
        self.__wav_obj = object
        self.__musicChoice = 0

    def playMusic(self):
        sa.stop_all()
        self.__wav_obj = sa.WaveObject.from_wave_file(self.__musicDirectory + self.__musicList[self.__musicChoice])
        play_obj = self.__wav_obj.play()

    def stopMusic(self):
        sa.stop_all()

    def nextMusic(self):
        sa.stop_all()
        self.__wav_obj = sa.WaveObject.from_wave_file(self.__musicDirectory + self.__musicList[musicChoice+1])
        play_obj = wav_obj.play()

    def checkMusic(self):
        for r, d, f in os.walk(self.__musicDirectory):
            for file in f:
                if file.endswith('.wav'):
                    self.__musicList.append(file)

    def setChoice(self, choice):
        self.__musicChoice = choice


    def getChoice(self):
        return self.__musicChoice

    musicChoice = property(getChoice,setChoice)



    #musicList = [file for r, d, f in os.walk(musicDirectory) for file in f if file.endswith('.mp3')]