import pandas as pd
import tensorflow as tf
from tensorflow.keras.preprocessing.text import Tokenizer
from tensorflow.keras.preprocessing.sequence import pad_sequences
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import LSTM,Dense, Dropout, SpatialDropout1D
from tensorflow.keras.layers import Embedding
from tensorflow.keras.models import load_model

model = load_model("model.h5")
df = pd.read_csv("./Tweets.csv")
tweet_df = df[['text','airline_sentiment']]
tweet_df = tweet_df[tweet_df['airline_sentiment'] != 'neutral']
sentiment_label = tweet_df.airline_sentiment.factorize()
sentiment_label
tweet = tweet_df.text.values
tokenizer = Tokenizer(num_words=5000)

def predict_sentiment(text):
    tw = tokenizer.texts_to_sequences([text])
    tw = pad_sequences(tw,maxlen=200)
    prediction = int(model.predict(tw).round().item())
    print("Predicted label: ", sentiment_label[1][prediction])

import argparse
parser = argparse.ArgumentParser()
parser.add_argument("-p", "-predict", action="store_true", help="Predict emotion in text")
parser.add_argument("text", help="Enter text", type=str)

args = parser.parse_args()
predict_sentiment(args.text)
