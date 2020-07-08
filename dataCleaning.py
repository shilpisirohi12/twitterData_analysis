import pandas as pd

twitter_df = pd.read_csv('tweets.csv')

# Dropping the duplicate tweets
twitter_df.drop_duplicates(subset ="id",
                     keep = False, inplace = True)
print(twitter_df.count())
def clean_tweets(columns):
    tweets=columns[0]

