import tweepy
import os
import time
import csv

# Twitter API credentials
consumer_key = "ZWrcOxxxxxxxxxxx"
consumer_secret = "cGhccSnxxxxxxxxxxxxxxxxrnhVFlY2gTfIBqQP"
access_token = "4273738-t0MEa3QffffffffffffEelfUwCJYQYrp"
access_secret = "g3dzzzzzzzzzzzzzzzzzzix0kceAg"

# Authentication to Twitter API
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_secret)

# Initialize the API
api = tweepy.API(auth)

# List of keywords to track
keywords = ['Beispieltext', 'sample text', 'texte dexemple']

# Define the Stream class
class Stream(tweepy.Stream):
    def __init__(self, *args, **kwargs):
        super().__init__(auth, *args, **kwargs)
        
    def on_status(self, status):
        # Check if the tweet contains one of the keywords
        if any(keyword in status.text.lower() for keyword in keywords):
            # Print the tweet details
            print('Account user:', status.user.name)
            print('Twitter handle:', status.user.screen_name)
            print('Tweet:', status.text)
            print('Time and date:', status.created_at)
            print('Previous mentions:')
            # Search for previous tweets from the same user containing the same keyword
            for tweet in tweepy.Cursor(api.user_timeline, screen_name=status.user.screen_name).items(100):
                if any(keyword in tweet.text.lower() for keyword in keywords):
                    print(tweet.text)
            print('\n\n')
            # Write the data to a CSV file
            with open('twitter_data.csv', 'a', newline='', encoding='utf-8') as file:
                writer = csv.writer(file)
                writer.writerow([status.user.name, status.user.screen_name, status.text, status.created_at])

# Create the Stream
stream = tweepy.Stream(auth=auth, tweet_mode='extended')

# Start the Stream
stream.filter(track=keywords)
