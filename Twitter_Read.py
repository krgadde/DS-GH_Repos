# -*- coding: utf-8 -*-
"""
Created on Thu Dec 27 11:00:31 2018

@author: karun
"""

import tweepy
from textblob import TextBlob


# Step 1 - Authenticate
consumer_key= 'WBwXRPsv8bLLXvZ3L6SKr1gab'
consumer_secret= 'Nx3JyUK8rb2OyGi3OOuJeq78sypYAYnxXDZ4DDrksuqBd5EIu3'

access_token='105876606-nR8C4LhQ49DB5MgTdJ0HRCClYOvErf1yAKO2yUGF'
access_token_secret='qw1vc8hxBDgGxA8c2zHMWZnyjTxAE2sjvg8HDV2RbbqCE'

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

#Step 3 - Retrieve Tweets
public_tweets = api.search('Trump')



#CHALLENGE - Instead of printing out each tweet, save each Tweet to a CSV file
#and label each one as either 'positive' or 'negative', depending on the sentiment 
#You can decide the sentiment polarity threshold yourself


for tweet in public_tweets:
    print(tweet.text)
    
    #Step 4 Perform Sentiment Analysis on Tweets
    analysis = TextBlob(tweet.text)
    print(analysis.sentiment)
    print("")