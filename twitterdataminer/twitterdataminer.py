import tweepy
from tweepy import OAuthHandler
import json
from io import FileIO

json_file = FileIO('../twitter_api_keys.json', mode='r')
json_object = json.load(json_file)

consumer_key = json_object['api_key']
consumer_secret = json_object['api_secret_key']
access_token = json_object['acces_token']
access_secret = json_object['access_token_secret']

auth = OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_secret)

api = tweepy.API(auth)

for status in tweepy.Cursor(api.home_timeline).items(10):
    # Process a single status
    print(status.text)
