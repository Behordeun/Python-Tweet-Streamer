#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jun 30 10:18:37 2022
Latest Update on Mon Jul  4 16:22 2022

@author: Muhammad
"""

##########################################################################
# 1. This Script will capture and save to MYSQL database (table), a stream of tweets according to the keyword(s) input by the user.
# 2. The file is saved as a into the database specified in the credentials script (keys.py)
# 3. If this script is run more than once with the same keyword, the database (table) with the keyword will be incremented
# 4. Script will run till and error is encountered in the stream or it is stopped with "Ctrl+C" twice.
##########################################################################

import mysql.connector
from mysql.connector import Error
import tweepy
import json
from dateutil import parser
import re
from transformers.pipelines import pipeline
from keys import consumer_key, consumer_secret, access_token, access_token_secret, host, password, database, user, charset, table

consumer_key = consumer_key
consumer_secret = consumer_secret
access_token = access_token
access_token_secret = access_token_secret
password = password


def connect(
        created_at,
        tweet_id,
        tweet_text,
        cleaned_tweet,
        source,
        username,
        retweet_count,
        followers_count,
        friends_count,
        listed_count,
        favourites_count,
        statuses_count,
        following,
        follow_request_sent,
        notifications,
        coordinates,
        place,
        location,
        sentiment_score,
        sentiment_label):
    """
    connect to MySQL database and insert twitter data
    """
    try:
        con = mysql.connector.connect(host=host,
                                      database=database, user=user, password=password, charset=charset)

        if con.is_connected():
            """
            Insert twitter data
            """
            cursor = con.cursor()
            # twitter, golf
            query = f"INSERT INTO {table} (created_at, tweet_id, tweet_text, cleaned_tweet, source, username, retweet_count, followers_count, friends_count, listed_count, favourites_count, statuses_count, following, follow_request_sent, notifications, coordinates, place, location, sentiment_score, sentiment_label) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
            cursor.execute(query, (
                created_at,
                tweet_id,
                tweet_text,
                cleaned_tweet,
                source,
                username,
                retweet_count,
                followers_count,
                friends_count,
                listed_count,
                favourites_count,
                statuses_count,
                following,
                follow_request_sent,
                notifications,
                coordinates,
                place,
                location,
                sentiment_score,
                sentiment_label
            ))
            con.commit()

    except Error as e:
        print(e)

    cursor.close()
    con.close()

    return

# Tweepy class to access Twitter API


class Streamlistener(tweepy.Stream):

    def on_connect(self):
        print("You are connected to the Twitter API, and currently streaming tweets into a MySQL database")

    def on_error(self):
        if status_code != 200:
            print("error found")
            # returning false disconnects the stream
            return False

    def clean_tweet(self, tweet):
        """
        Clean the tweet text by removing links, special characters, hashtags, etc.
        Create a new attribute called 'cleaned_tweet' that contains the clean tweet text
        """
        tweet = re.sub('https://\\S+', '', tweet)  # remove all https links
        tweet = re.sub('http://\\S+', '', tweet)  # remove all http links
        # remove all special characters
        tweet = re.sub('[^A-Za-z]+', ' ', tweet)
        return tweet

    def sentiment_analyzer_score(self, tweet):
        """
        This will use the transformers sentiment analysis pipeline to analyze the tweet.
        """
        sentiment = pipeline('sentiment-analysis', model="distilbert-base-uncased-finetuned-sst-2-english",
                             tokenizer="distilbert-base-uncased-finetuned-sst-2-english")
        analysis = sentiment([tweet])
        return analysis[0]['score']

    def sentiment_analyzer_label(self, tweet):
        """
        This will use the transformers sentiment analysis pipeline to analyze the tweet.
        """
        sentiment = pipeline('sentiment-analysis', model="distilbert-base-uncased-finetuned-sst-2-english",
                             tokenizer="distilbert-base-uncased-finetuned-sst-2-english", )
        analysis = sentiment([tweet])
        return analysis[0]['label']

    def on_data(self, data):
        """This method reads in tweet data as Json and extracts the data we want."""
        try:
            raw_data = json.loads(data)

            if 'text' in raw_data:
                created_at = parser.parse(raw_data['created_at'])
                tweet_id = raw_data['id']
                tweet_text = raw_data['text']
                cleaned_tweet = self.clean_tweet(raw_data['text'])
                source = raw_data['source'].split('>')[1].split('<')[0]
                username = raw_data['user']['screen_name']
                retweet_count = raw_data['retweet_count']
                followers_count = raw_data['user']['followers_count']
                friends_count = raw_data['user']['friends_count']
                listed_count = raw_data['user']['listed_count']
                favourites_count = raw_data['user']['favourites_count']
                statuses_count = raw_data['user']['statuses_count']
                following = raw_data['user']['following']
                follow_request_sent = raw_data['user']['follow_request_sent']
                notifications = raw_data['user']['notifications']
                coordinates = raw_data['coordinates']
                if raw_data['place'] is not None:
                    place = raw_data['place']['country']
                    print(place)
                else:
                    place = None
                location = raw_data['user']['location']
                sentiment_score = self.sentiment_analyzer_score(
                    self.clean_tweet(raw_data['text']))
                sentiment_label = self.sentiment_analyzer_label(
                    self.clean_tweet(raw_data['text']))

                # insert data just collected into MySQL database
                connect(
                    created_at,
                    tweet_id,
                    tweet_text,
                    cleaned_tweet,
                    source,
                    username,
                    retweet_count,
                    followers_count,
                    friends_count,
                    listed_count,
                    favourites_count,
                    statuses_count,
                    following,
                    follow_request_sent,
                    notifications,
                    coordinates,
                    place,
                    location,
                    sentiment_score,
                    sentiment_label)
                print("Tweet colleted at: {} ".format(str(created_at)))
        except Error as e:
            print(e)


if __name__ == '__main__':

    # authentication so we can access twitter
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    api = tweepy.API(auth, wait_on_rate_limit=True)

    # create instance of Streamlistener
    listener = Streamlistener(
        consumer_key, consumer_secret, access_token, access_token_secret)
    #stream = tweepy.Stream(auth = api.auth, listener=listener)

    track = []
    # Input number of elements
    track = [item for item in input(
        "Enter the list of keywords to track : ").split(',')]
    print(f'We are tracking tweets on {track}')

    listener.filter(track=track)  # , languages=['en'])
