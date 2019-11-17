from flask import Flask,render_template,request
import tweepy
from textblob import TextBlob

consumer_key= 'CONSUMER_KEY'
consumer_secret= 'CONSUMER_SECRET KEY'

access_token='ACCESS TOKEN'
access_token_secret='ACCESS_TOKEN_SECRET KEY'

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

app =Flask(__name__)

@app.route("/")
def index():
	return render_template("index.html")

@app.route("/Analaysis",methods=["POST"])
def Analysis():
	name=request.form.get("name")
	public_tweets = api.search(name)
	Tweets=[tweet.text for tweet in public_tweets]
	return render_template("Analysis.html",Tweets=Tweets)

if __name__ == '__main__':
	app.run(debug=True)
	

