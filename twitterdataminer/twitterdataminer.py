import tweepy
from tweepy import OAuthHandler
from tweepy import Stream
from tweepy.streaming import StreamListener
import json

with open('../twitter_api_keys.json') as f:
    json_object = json.load(f)

consumer_key = json_object['api_key']
consumer_secret = json_object['api_secret_key']
access_token = json_object['access_token']
access_secret = json_object['access_token_secret']

auth = OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_secret)

api = tweepy.API(auth)


class MyListener(StreamListener):
    def on_data(self, raw_data):
        try:
            with open('tweets.json', 'a') as f:
                f.write(raw_data)
                return True
        except BaseException as e:
            print("Error on_data: %s" % str(e))
        return True

    def on_error(self, status_code):
        print(status_code)
        return True


twitter_stream = Stream(auth, MyListener())
twitter_stream.filter(track=['Boris'])
