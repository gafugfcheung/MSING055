import tweepy
from tweepy import OAuthHandler
import json

# Credentials
consumer_key = "YOUR_CONSUMER_KEY"
consumer_secret = "YOUR_CONSUMER_SECRET"
access_token = "YOUR_ACCESS_TOKEN"
access_token_secret = "YOUR_ACCESS_TOKEN_SECRET"

# Authentication
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

# Scraping the data
for status in tweepy.Cursor(api.search, q='diabetes').items(1):
	json_str = status._json
	print json.dumps(json_str, indent=4, sort_keys=True)
