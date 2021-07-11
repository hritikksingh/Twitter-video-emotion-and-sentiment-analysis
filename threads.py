import imageio
import moviepy.editor
from moviepy.video.VideoClip import VideoClip
import os
from pydub import AudioSegment
import wave
from threading import Thread
from text_emotion import get_text_sentiment
from speech_emotion import get_speech_emotion
from video_emotion import get_video_emotion
import glob
import queue

def reducequality():
    sound = AudioSegment.from_wav("converted.wav")
    sound = sound.set_channels(1)
    sound.export("audio/converted.wav", format="wav")


def covertingfile():
    file_name=glob.glob("./input/*")[0]
    video1=moviepy.editor.VideoFileClip(file_name)
    audio=video1.audio
    audio.write_audiofile("converted.wav")
    video2=moviepy.editor.VideoFileClip(file_name)
    clip = video2.without_audio()
    clip.write_videofile("video/converted.mp4")


def main():
    covertingfile()
    reducequality()
    
    que=queue.Queue()
    
    t1 = Thread(target=lambda q, arg1: q.put(get_video_emotion), args=(que, 'world!'))
    t2 = Thread(target=lambda q, arg1: q.put(get_text_sentiment), args=(que, 'world!'))
    t3 = Thread(target=lambda q, arg1: q.put(get_speech_emotion), args=(que, 'world!'))
    
    t1.start()
    t2.start()
    t3.start()
    
    t1.join()    
    t2.join()
    t3.join()
    
    output={}
    result=que.get()
    output['video']=result()
    
    result=que.get()
    data=result()
    output['text']=dict(data.values)
    
    result=que.get()
    output['speech']=str(result())
    
    return output

