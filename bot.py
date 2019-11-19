import tweepy
from keys import *

# Authenticate to Twitter
auth = tweepy.OAuthHandler(twitter_APIkey,
    twitter_APISecretKey)
auth.set_access_token(twitter_AccessToken,
    twitter_AccessTokenSecret)

api = tweepy.API(auth)

try:
    api.verify_credentials()
    print("Authentication OK")
    api.update_status("Test tweet from Tweepy Python")
except:
    print("Error during authentication")
