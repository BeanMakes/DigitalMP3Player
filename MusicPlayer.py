import os
from pydub import AudioSegment
from pydub.playback import play

musicList = []
musicDirectory = './Music/'

#musicDirectory + musicList[choice]

def playMusic(choice):
    sound = AudioSegment.from_mp3(musicDirectory + musicList[choice])
    play(sound)


def creatFolder(directory):
    try:
        if not os.path.exists(directory):
            os.makedirs(directory)
    except OSError:
        print('Error: Creating directory. ' + directory)


def checkMusic():
    for r, d, f in os.walk(musicDirectory):
        for file in f:
            if file.endswith('.mp3'):
                musicList.append(file)


creatFolder(musicDirectory)
checkMusic()
print(musicList)
playMusic(0)