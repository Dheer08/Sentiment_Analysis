import tweepy
from textblob import TextBlob

# Step 1 - Authenticate
consumer_key= 'Yihd0uVqliPaxgzEoXcMhXAT6'
consumer_secret= '8MuOuWyoeNtu1KqN8p6EAgXNGLPx2NfqB8T8Poa6ZLPP1e8Tdi'

access_token='1183614099374034944-MSYEG2CEhqh24QO9iRcL4LzlfMvC2I'
access_token_secret='GBG0TJGW4jtc1uqJtRG8pFxdoYuEKBHNG2IF61To7lWhj'

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

#Step 3 - Retrieve Tweets
public_tweets = api.search('Trump')



for tweet in public_tweets:
    print(tweet.text)
    #Step 4 Perform Sentiment Analysis on Tweets
    #analysis = TextBlob(tweet.text)
    #print(analysis.sentiment)
    #print("")