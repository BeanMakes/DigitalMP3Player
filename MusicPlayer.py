from pydub import AudioSegment

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
        print(self.__musicChoice)

    def nextMusic(self):
        sa.stop_all()
        self.__musicChoice = self.__musicChoice +1
        self.__wav_obj = sa.WaveObject.from_wave_file(self.__musicDirectory + self.__musicList[self.__musicChoice])
        play_obj = self.__wav_obj.play()

    def preMusic(self):
        if self.__musicChoice == 0:
            self.__musicChoice = 0
        else:
            sa.stop_all()
            self.__musicChoice = self.__musicChoice - 1
            self.__wav_obj = sa.WaveObject.from_wave_file(self.__musicDirectory + self.__musicList[self.__musicChoice])
            play_obj = self.__wav_obj.play()

    def checkMusic(self):
        for r, d, f in os.walk(self.__musicDirectory):
            for file in f:
                if file.endswith('.mp3'):
                    wav_audio = AudioSegment.from_file(self.__musicDirectory+file, format="wav")
                    wav_audio.export(self.__musicDirectory+file.replace('.mp3', '') + ".wav", format="wav")
        for r, d, f in os.walk(self.__musicDirectory):
            for file in f:
                if file.endswith('.wav'):
                    self.__musicList.append(file)
        for r, d, f in os.walk(self.__musicDirectory):
            for file in f:
                if not file.endswith('.wav'):
                    os.remove(self.__musicDirectory+file)

    def setChoice(self, choice):
        self.__musicChoice = choice

    def getChoice(self):
        return self.__musicChoice

    musicChoice = property(getChoice,setChoice)



    #musicList = [file for r, d, f in os.walk(musicDirectory) for file in f if file.endswith('.mp3')]