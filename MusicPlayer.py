from pydub import AudioSegment

import os
import simpleaudio as sa
import wave
import time
import numpy as np
from scipy.io import wavfile

import matplotlib.pyplot as plt

# Class for the Music Player
class MusicPlayer:

    # Intialising variables for the class
    def __init__(self):
        self.__time = time.time()
        self.__musicList = []
        self.__musicDirectory = './Music/'
        self.__wav_obj = sa.WaveObject
        self.__musicChoice = 0
        self.__size = 0
        

    def playMusic(self):
        sa.stop_all()
        self.__wav_obj = sa.WaveObject.from_wave_file(self.__musicDirectory + self.__musicList[self.__musicChoice])
        self.__sampleRate, self.__audioData = wavfile.read(self.__musicDirectory + self.__musicList[self.__musicChoice])
        play_obj = self.__wav_obj.play()

        waveFile = wave.open(self.__musicDirectory + self.__musicList[self.__musicChoice])
        self.__size = waveFile.getnframes()
        waveFile.close()

    def stopMusic(self):
        sa.stop_all()

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
        # Checks if there are any .mp3 files
        for r, d, f in os.walk(self.__musicDirectory):
            for file in f:
                if file.endswith('.mp3'):
                    wav_audio = AudioSegment.from_file(self.__musicDirectory+file, format="wav")
                    wav_audio.export(self.__musicDirectory+file.replace('.mp3', '') + ".wav", format="wav")
                    # Exports them to become .wav files
        for r, d, f in os.walk(self.__musicDirectory):
            for file in f:
                if file.endswith('.wav'):
                    self.__musicList.append(file)
                    # Stores list of music into the list
        for r, d, f in os.walk(self.__musicDirectory):
            for file in f:
                if not file.endswith('.wav'):
                    os.remove(self.__musicDirectory+file)
                    # Detects and deletes any files that are not .wav files

    def setChoice(self, choice):
        self.__musicChoice = choice

    def getChoice(self):
        return self.__musicChoice

    def setMusicList(self, musicList):
        self.__musicList = musicList

    def getMusicList(self):
        return self.__musicList

    def setSize(self, size):
        self.__size = size

    def getSize(self):
        return self.__size

    def getPlayObj(self):
        return self.__wav_obj.play()
    
    def getTotalTimeSong(self):
        return np.arange(len(self.__audioData)) / self.__sampleRate
    
    def getMusicName(self):
        return self.__musicList[self.__musicChoice]
    
    def plotGraph(self):
        plt.figure(figsize=(10, 4))
        plt.plot(np.arange(len(self.__audioData)) / self.__sampleRate, self.__audioData)
        plt.xlabel('Time (s)')
        plt.ylabel('Amplitude')
        plt.title('Audio Waveform')
        plt.show()
