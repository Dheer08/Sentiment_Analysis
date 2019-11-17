from flask import Flask,render_template,request
import tweepy
from textblob import TextBlob

consumer_key= 'zUmiKqDKQetRtcTeBF7gX5wED'
consumer_secret= 'ET81cuG14RRjXRNhoNKWevMlJMFIMxiMQe2ttZMLOiZpSKXuFO'

access_token='1183614099374034944-AOShuxm8v4XUTRpLnlKSwg5xWpfuy7'
access_token_secret='8KjvzEgF1KcBjKrdKQsiZKDB8JlTGAIFxRb8k6nmhyoQ4'

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
	

