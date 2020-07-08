import tweepy
import json
import csv
import time

# Load Twitter API secrets from an external JSON file
secrets = json.loads(open('twitter_keys.json').read())
api_key = secrets['api_key']
api_secret_key = secrets['api_secret_key']
access_token = secrets['access_token']
access_token_secret = secrets['access_token_secret']


# Connect to Twitter API using the secrets
auth = tweepy.OAuthHandler(api_key, api_secret_key)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth,wait_on_rate_limit=True, wait_on_rate_limit_notify=True)

# test authentication
try:
    api.verify_credentials()
    print("Authentication OK")
except:
    print("Error during authentication")

# Fetching Data
def fetch_data(queryString):
    twitter_data=[]
    count=1
    for row in tweepy.Cursor(api.search, q=queryString, tweet_mode="extended", lang="en",result_type="recent").items(1000):
    # data = api.search(q=queryString,tweet_mode='extended', lang="en",result_type='recent', count=5)
        print(count)
        print(row)
        row_data=[]
        row_data.extend((row.created_at,row.id))
        str = ''
        for x in row.entities:
            if x == 'hashtags':
                for y in row.entities[x]:
                    str=str + y['text']+','
            #print(str)
        row_data.append(str)
        try:
            row_data.append(row.retweeted_status.full_text)
        except AttributeError:
            row_data.append(row.full_text)
        twitter_data.append(row_data)
        count=count+1
    print(twitter_data)
    # opening the csv file in 'w+' mode
    file = open('tweets.csv', 'w+',encoding="utf-8", newline='')

    # writing the data into the file
    with file:
        write = csv.writer(file)
        write.writerows(twitter_data)


fetch_data("COVID19")
# print(data[0].created_at, data[0].id, data[0].full_text, data[0].entities['hashtags'], end="\n***********************************\n")
# print(data[0].retweeted_status.full_text,data[0].retweeted_status.id, end="\n*************************\n")
# print(data[0].retweeted_status)