import tweepy
import requests
import json
import locale
import sys
from keys import *
from tweepy import Stream
from tweepy.streaming import StreamListener
import urllib.request
import threads 
import remove

class StdOutListener(StreamListener):
    def on_data(self,data):
        clean_data = json.loads(data)
        video_links_list=clean_data['extended_entities']['media'][0]['video_info']['variants']
        video_link=""
        for item in video_links_list:
            if item['content_type']=="video/mp4":
                video_link=item['url']
                break
        name="./input/input.mp4"
        print(video_link)
        try:
            print("Downloading starts...\n")
            urllib.request.urlretrieve(video_link, name)
            print("Download completed..!!")
            output=threads.main()
            tweet=createTweet(output)
            print("tweet created!!")
            replyToTweet(tweet,clean_data['id'])
            print("Tweeted Successfully..!!")
            remove.removeFile()
            
        except Exception as e:
            print(e)


    def on_error(self, status_code):
        if status_code == 420:
            #returning False in on_error disconnects the stream
            return False	

def setAuth():
	auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
	auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
	api = tweepy.API(auth)
	return api,auth

def followStream():
	listener = StdOutListener()
	stream = Stream(auth,listener)
	stream.filter(track=[ACCOUNT_NAME])

def replyToTweet(tweet,tweet_id):
	api.update_status(tweet,in_reply_to_status_id =tweet_id,auto_populate_reply_metadata =True)

def createTweet(output):
    output['video']=dict((sorted(output['video'].items(), key=lambda item: item[1],reverse=True)))
    output['text']=dict((sorted(output['text'].items(), key=lambda item: item[1],reverse=True)))

    count=0
    temp=""
    for key,value in output['video'].items():
        temp=temp+key.title()
        temp=temp+" ("+str(int(value))+"%) "
        temp+="  "
        count+=1
        if count==3:
            break;
    output['video']=temp

    count=0
    temp=""
    for key,value in output['text'].items():
        temp=temp+key.title()
        temp=temp+" ("+str(int(value))+"%) "
        temp+=" "
        count+=1
        if count==3:
            break;
    output['text']=temp

    tweet=f"""
    Analysis Output:
Video Analysis: {output['video']}
Speech text Analysis: {output['text']}
Speech Voice Analysis: {output['speech'].title()}
    """
    return tweet

if __name__=="__main__":
    ACCOUNT_NAME='emosentiBot'
    api,auth = setAuth()
    followStream()
    



    
    
