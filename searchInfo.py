import tweepy
import csv
from datetime import datetime
import datetime


auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secrete)

api = tweepy.API(auth)
tweets_for_csv = []
                                         #="parametro da cercare"                                          #numero di tweet ( Massimo numero = 100 ) 
public_tweets = tweepy.Cursor(api.search, q="covid", result_type="mixed", tweet_mode="extended", lang='it').items(1)

d = datetime.datetime.now()
def noZeroDay(hour, minute, second):
    # method for add 0 if hour || minute == 1
    h = ''
    m = ''
    if len(str(hour)) == 1:
        h = str( '0' + hour )
    elif len(str(hour)) > 1: 
        h = str(hour)
    if len(str(minute)) == 1:
        m = str( '0' + minute )
    elif len(str(minute)) > 1:
        m = str(minute)
    return str(h) + '-' + str(m) + '-' + str(second)

timestamp = str(datetime.date.today()) + '--' + noZeroDay(d.hour,d.minute,d.second)

# for all tweet, push them in the array for create after a csv file
for tweet in public_tweets:
  tweets_for_csv.append([tweet.full_text])
  
# create the name of the file, example: 2020-10-20--18-22-33_tweets.csv
outfile = timestamp + "_tweets.csv"
with open(outfile, 'w+', encoding='utf-8') as file:
    writer = csv.writer(file, delimiter=',')
    writer.writerow(['COMMENTI,'])
    writer.writerows(tweets_for_csv)
