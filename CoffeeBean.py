import tweepy
from os import environ
from dotenv import load_dotenv


'''
setting up an API instance
'''

#Obtaining OAuth keys
load_dotenv()
api_key = environ["API_KEY"]
api_key_secret = environ["API_KEY_SECRET"]
access_token = environ["ACCESS_TOKEN"]
access_token_secret = environ["ACCESS_TOKEN_SECRET"]

# Setting up the authenticator 
authenticator = tweepy.OAuthHandler(api_key, api_key_secret)
authenticator.set_access_token(access_token, access_token_secret)

#Setting up the API instance
api = tweepy.API(authenticator, wait_on_rate_limit = True)