import os
import simpleaudio as sa


musicList = []
musicDirectory = './Music/'
wav_obj = object
musicIsPlaying = False


def playMusic(choice):
    wav_obj = sa.WaveObject.from_wave_file(musicDirectory + musicList[choice])
    play_obj = wav_obj.play()
    musicPlaying = play_obj.is_playing()
    play_obj.wait_done()


def creatFolder(directory):
    try:
        if not os.path.exists(directory):
            os.makedirs(directory)
    except OSError:
        print('Error: Creating directory. ' + directory)


def checkMusic():
    for r, d, f in os.walk(musicDirectory):
        for file in f:
            if file.endswith('.wav'):
                musicList.append(file)

    #musicList = [file for r, d, f in os.walk(musicDirectory) for file in f if file.endswith('.mp3')]


def isMusicRunning():
    return musicIsPlaying


creatFolder(musicDirectory)
checkMusic()