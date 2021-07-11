import os

def removeFile():
    os.remove('converted.wav')
    os.remove('./input/input.mp4')
    os.remove('./audio/converted.wav')
    os.remove('./video/converted.mp4')
