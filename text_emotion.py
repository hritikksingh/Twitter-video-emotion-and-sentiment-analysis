import preprocessor as p
import numpy as np 
import pandas as pd 
import emoji
import transformers
from tqdm.notebook import tqdm
from tokenizers import Tokenizer, models, pre_tokenizers, decoders, processors
from tensorflow.keras.preprocessing import sequence, text
from tensorflow.keras.models import model_from_json,model_from_yaml
from tqdm import tqdm
import pickle
import speech_recognition as sr
import glob



# Misspelled data
a_file=open("./data/text/aspell.pkl","rb")
miss_corr = pickle.load(a_file)


def misspelled_correction(val):
    for x in val.split(): 
        if x in miss_corr.keys(): 
            val = val.replace(x, miss_corr[x]) 
    return val



#Contractions

contractions = pd.read_csv("./data/text/contractions.csv")
cont_dic = dict(zip(contractions.Contraction, contractions.Meaning))


def cont_to_meaning(val): 
  
    for x in val.split(): 
        if x in cont_dic.keys(): 
            val = val.replace(x, cont_dic[x]) 
    return val





#Punctuations and emojis

def punctuation(val): 
  
    punctuations = '''()-[]{};:'"\,<>./@#$%^&_~'''
  
    for x in val.lower(): 
        if x in punctuations: 
            val = val.replace(x, " ") 
    return val




def clean_text(val):
    val = misspelled_correction(val)
    val = cont_to_meaning(val)
    val = p.clean(val)
    val = ' '.join(punctuation(emoji.demojize(val)).split())
    
    return val



#assigning id to each sentiment
sent_to_id  = {"empty":0, "sadness":1,"enthusiasm":2,"neutral":3,"worry":4,
                        "surprise":5,"love":6,"fun":7,"hate":8,"happiness":9,"boredom":10,"relief":11,"anger":12}


token=pickle.load(open("./data/text/token.pkl","rb"))
max_len = 160



def speech_to_text():    
    r = sr.Recognizer()  
    file = glob.glob('./audio/*')[0]
    with sr.AudioFile(file) as source:
        audio = r.record(source)
        text = r.recognize_google(audio)   
    
    return text;


def get_text_sentiment():
    yaml_file = open('./data/text/model.yaml', 'r')
    loaded_model_yaml = yaml_file.read()
    yaml_file.close()
    model = model_from_yaml(loaded_model_yaml)
    # load weights into new model
    model.load_weights("./data/text/model.h5")
    
    text=speech_to_text()
    text = clean_text(text)
    #tokenize
    twt = token.texts_to_sequences([text])
    twt = sequence.pad_sequences(twt, maxlen=max_len, dtype='int32')
    sentiment = model.predict(twt,batch_size=1,verbose = 2)
    sent = np.round(np.dot(sentiment,100).tolist(),0)[0]
    result = pd.DataFrame([sent_to_id.keys(),sent]).T
    result.columns = ["sentiment","percentage"]
    result=result[result.percentage !=0]
    return result






