import os

musicList = []
musicDirectory = './Music/'


def play(choice):
    os.system(musicDirectory + musicList[choice])


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
play(0)