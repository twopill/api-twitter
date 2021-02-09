import tweepy
import sys
import csv

from twitter_app_credentials import *

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secrete)
api = tweepy.API(auth)
                                          #al posto di "covid" metti la parola che ti interessa cercare
public_tweets = tweepy.Cursor(api.search, q="codiv", result_type="mixed", tweet_mode="extended").items(numeroditweetchevuoi)

for tweet in public_tweets:
  print("@"tweet.user.screen_name
  tweet_text = tweet.full_text)
  
#non toccare

		tweets_for_csv.append([username, tweet.id_str, tweet.created_at, tweet.text.encode("utf-8")])

	
	  outfile = username + "_tweets.csv"
	  print "writing to " + outfile
	  with open(outfile, 'w+') as file:
		writer = csv.writer(file, delimiter=',')
		writer.writerows(tweets_for_csv)
