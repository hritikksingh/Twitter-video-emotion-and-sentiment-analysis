import librosa
import soundfile
import pickle
import wave
import os, glob, pickle
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.neural_network import MLPClassifier
from sklearn.metrics import accuracy_score

#extract features from video
def extract_feature(file_name, mfcc, chroma, mel):
    with soundfile.SoundFile(file_name) as sound_file:
        X = sound_file.read(dtype="float32")
        sample_rate=sound_file.samplerate
        if chroma:
            stft=np.abs(librosa.stft(X))
            result=np.array([])
        if mfcc:
            mfccs=np.mean(librosa.feature.mfcc(y=X, sr=sample_rate, n_mfcc=40).T, axis=0)
            result=np.hstack((result, mfccs))
        if chroma:
            chroma=np.mean(librosa.feature.chroma_stft(S=stft, sr=sample_rate).T,axis=0)
            result=np.hstack((result, chroma))
        if mel:
            mel=np.mean(librosa.feature.melspectrogram(X, sr=sample_rate).T,axis=0)
            result=np.hstack((result, mel))
    return result

#main function to predict the emotion
def get_speech_emotion():
    Pkl_Filename = "./data/speech/Emotion_Voice_Detection_Model.pkl"  
    with open(Pkl_Filename, 'rb') as file:  
        Emotion_Voice_Detection_Model = pickle.load(file)
    
    file = glob.glob('./audio/*')[0]
    ans =[]
    new_feature  = extract_feature(file, mfcc=True, chroma=True, mel=True)
    ans.append(new_feature)
    ans = np.array(ans)

    emotion=Emotion_Voice_Detection_Model.predict(ans)
    return emotion[0]

