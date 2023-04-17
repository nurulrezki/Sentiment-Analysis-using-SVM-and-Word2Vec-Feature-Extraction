# Import Libraries
import tweepy
import csv

# Authentication
consumer_key = 'your consumer key'
consumer_secret = 'your consumer secret'
access_token ='ypur access token'
access_token_secret ='ypur access token secret'
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth,wait_on_rate_limit=True)
api = tweepy.API(auth)

#defined csv file
csvFile = open('dataset.csv', 'a')
csvWriter = csv.writer(csvFile)

tweets = api.search_tweets(q="Kampus Merdeka",since_id=50, lang="id")
for tweet in tweets:
    print (tweet.created_at, tweet.text)
    csvWriter.writerow([tweet.created_at, tweet.text.encode('utf-8')])

print("Berikut ini adalah 5 twit terkahir")
i=1
for tweet in tweets[:5]:
    print(str(i) +') '+ tweet.text + '\n')
    i= i+1