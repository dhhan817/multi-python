from __future__ import print_function
import tweepy
import json
from pymongo import MongoClient
 
MONGO_HOST= 'mongodb://localhost/twitterdb'  
                                             
 
WORDS = ['#bigdata', '#AI', '#datascience', '#machinelearning', '#ml', '#iot']
 
CONSUMER_KEY = "..."
CONSUMER_SECRET = "..."
ACCESS_TOKEN = "..."
ACCESS_TOKEN_SECRET = "."
 
 
class StreamListener(tweepy.StreamListener):    
 
    def on_connect(self):
        print("You are now connected to the streaming API.")
 
    def on_error(self, status_code):
        print('An Error has occured: ' + repr(status_code))
        return False
 
    def on_data(self, data):
        #TODO
 
#TODO
