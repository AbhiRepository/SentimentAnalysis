import tweepy
import sentiment_mod as s


consumer_key = 'Mau4Avgh41GX1Jn5kZ5uvQUWI'
consumer_secret = 'MLdiQne55btJIL5z1vEFRaSeHhwkLUfaGPqO1YPQTtCdiSZA12'

access_token = '902339453158436865-KMVKojyAcEGSErOYgc2LmnwJ1lGLLZt'
access_token_secret = '2a4g3o55LNYVB7peF3WxlqPZwfuE53iPhUcxRnxa1RChR'

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

public_tweets = api.search('Annabelle: Creation')

for tweet in public_tweets:
	print(tweet.text)
	print(s.sentiment(tweet.text))
	
