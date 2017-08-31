import tweepy
import sentiment_mod as s


consumer_key = '****'
consumer_secret = '***'

access_token = '****'
access_token_secret = '***'

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

public_tweets = api.search('*** Anytopic you like****')

for tweet in public_tweets:
	print(tweet.text)
	print(s.sentiment(tweet.text))
	
