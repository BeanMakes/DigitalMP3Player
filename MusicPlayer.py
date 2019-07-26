from pydub import AudioSegment

import os
import simpleaudio as sa
import wave
import time
import threading

#Class for the Music Player
class MusicPlayer:

    #Intialising variables for the class
    def __init__(self):
        self.__time = time.time()
        self.__musicList = []
        self.__musicDirectory = './Music/'
        self.__wav_obj = object
        self.__musicChoice = 0

    def playMusic(self):
        sa.stop_all()
        self.__wav_obj = sa.WaveObject.from_wave_file(self.__musicDirectory + self.__musicList[self.__musicChoice])
        play_obj = self.__wav_obj.play()

        waveFile = wave.open(self.__musicDirectory + self.__musicList[self.__musicChoice])
        print(waveFile.getnframes())
        #threading.Thread(target=stopwatch(waveFile.getnframes()/44234)).start() #Song length (by time) calculation
        waveFile.close()

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
        #Checks if there are any .mp3 files
        for r, d, f in os.walk(self.__musicDirectory):
            for file in f:
                if file.endswith('.mp3'):
                    wav_audio = AudioSegment.from_file(self.__musicDirectory+file, format="wav")
                    wav_audio.export(self.__musicDirectory+file.replace('.mp3', '') + ".wav", format="wav")
                    #Exports them to become .wav files
        for r, d, f in os.walk(self.__musicDirectory):
            for file in f:
                if file.endswith('.wav'):
                    self.__musicList.append(file)
                    #Stores list of music into the list
        for r, d, f in os.walk(self.__musicDirectory):
            for file in f:
                if not file.endswith('.wav'):
                    os.remove(self.__musicDirectory+file)
                    #Detects and deletes any files that are not .wav files

    def setChoice(self, choice):
        self.__musicChoice = choice

    def getChoice(self):
        return self.__musicChoice

    def getMusicList(self):
        return self.__musicList

    musicChoice = property(getChoice,setChoice)

def stopwatch(seconds):
    start = time.time()
    time.clock()
    elapsed = 0
    while elapsed < seconds:
        elapsed = time.time() - start
        print("loop cycle time: %f, seconds count: %02d" % (time.clock(), elapsed))
        time.sleep(1)


    #musicList = [file for r, d, f in os.walk(musicDirectory) for file in f if file.endswith('.mp3')]