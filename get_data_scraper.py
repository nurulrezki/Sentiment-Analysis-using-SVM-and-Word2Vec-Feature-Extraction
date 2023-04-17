import os

# Using OS library to call CLI commands in Python
#os.system("snscrape --jsonl --max-results 50  twitter-search \"Kampus Merdeka\" > text-query-tweets.json")

import snscrape.modules.twitter as sntwitter
import pandas as pd

# Creating list to append tweet data to
tweets_list1 = []

# Using TwitterSearchScraper to scrape data and append tweets to list
for i,tweet in enumerate(sntwitter.TwitterSearchScraper('Kampus Merdeka since:2021-11-21 until:2022-03-20').get_items()):
    if i>500:
        break
    tweets_list1.append([tweet.date, tweet.id, tweet.content, tweet.user.username])
    
# Creating a dataframe from the tweets list above 
tweets_df1 = pd.DataFrame(tweets_list1, columns=['Datetime', 'Tweet Id', 'Text', 'Username'])

# Show data frame
#print(tweets_df1)

#expor dataframe to csv file
tweets_df1.to_csv('dataset_batch26.csv')