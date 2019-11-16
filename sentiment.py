import tweepy
from textblob import TextBlob

# Step 1 - Authenticate
consumer_key= 'CONSUMER_KEY'
consumer_secret= 'CONSUMER_SECRET KEY'

access_token='ACCESS TOKEN'
access_token_secret='ACCESS_TOKEN_SECRET KEY'

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