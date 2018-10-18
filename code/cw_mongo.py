from __future__ import print_function
import tweepy
import json
from pymongo import MongoClient
 
MONGO_HOST= 'mongodb://localhost/twitterdb' #if port not 27017, port must be specified
                                             
 
WORDS = ['#bigdata', '#AI', '#datascience', '#machinelearning', '#ml', '#iot'] #Words to track
 
CONSUMER_KEY = "YOUR_OWN_CONSUMER_KEY"
CONSUMER_SECRET = "YOUR_OWN_CONSUMER_SECRET"
ACCESS_TOKEN = "YOUR_OWN_ACCESS_TOKEN"
ACCESS_TOKEN_SECRET = "YOUR_OWN_ACCESS_TOKEN_SECRET"
 
#tweepy.StreamListener must be inherited to own class if on_data should be modified
#Code below overrides on_connect, on_error, on_data
class StreamListener(tweepy.StreamListener):    
 
    def on_connect(self):
        print("You are now connected to the streaming API.")
 
    def on_error(self, status_code):
        print('An Error has occured: ' + repr(status_code))
        return False
    
    #Search for on_data at the documentation
    #on_data goes on when raw data is received from StreamListener
    def on_data(self, data):
        try:
            #Connecting to MongoClient can be moved to on_connect
            client = MongoClient(MONGO_HOST) #MongoDB server must be running at this time
            db = client.twitterdb
            datajson = json.loads(data) #Twitter returns json. Thus load json
            created_at = datajson['created_at'] #Show when tweet is collected
            print("Tweet collected at" + str(created_at)) 
            db.twitter_search.insert(datajson) #Insert loaded json file to MongoDB
        except Exception as e:
            print(e)
 
auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET) 
auth.set_access_token(ACCESS_TOKEN,ACCESS_TOKEN_SECRET)

listener = StreamListener(api=tweepy.API(wait_on_rate_limit=True)) #Creating streamlistener object
streamer = tweepy.Stream(auth=auth, listener=listener)
print("Tracking: " + str(WORDS))
streamer.filter(track=WORDS) #Streamer tracks specified word list
