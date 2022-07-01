# -*- coding: utf-8 -*-
"""
Created on Tue Jun 19 11:18:37 2018
Latest Update on Sun Jun 26 2022

Updated to support tweepy v4 and continue supporting v3 on Thursday June 6 16:33 WAT
Updated to fix multiple file creation bug on Sunda June 26 2022

@author: Behordeun
"""
##########################################################################
# 1. This Script will capture and save to file, a stream of tweets according to the keyword(s) input by the user.
# 2. The file is saved as a "keyword.json"
# 3. If this script is run more than once with the same keyword, the initial file saved with the keyword will be incremented
# 4. Script will run till and error is encountered in the stream or it is stopped with "Ctrl+C" twice.
##########################################################################

import tweepy
from datetime import datetime as dt
import pandas as pd
from datetime import datetime as dt
from keys import consumer_key, consumer_secret, access_token, access_token_secret, host, password, database, user, charset

consumer_key = consumer_key
consumer_secret = consumer_secret
access_token = access_token
access_token_secret = access_token_secret
password = password


def connect(
        tweet_id,
        tweet_text,
        hashtags,
        source,
        username,
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
        location):
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
            query = "INSERT INTO elections (id, tweet_text, hashtags, source, username, followers_count, friends_count, listed_count, favourites_count, statuses_count, following, follow_request_sent, notifications, coordinates, place, location) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
            cursor.execute(query, (
                tweet_id,
                tweet_text,
                hashtags,
                source,
                username,
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
                location))
            con.commit()

    except Error as e:
        print(e)

    cursor.close()
    con.close()

    return


Tracker = ['Atiku', 'Kwakwanso', 'Peter Obi', 'Tinubu']
# Tracker=input('What are we tracking on Twitter?: ')

try:
    tweepy_version = int(tweepy.__version__[0])
except Exception as e:
    print(
        f"Error while determining the version of tweepy you are working with.\nDetails => {e} ")

if tweepy_version == 4:
    time_obj_str = dt.strftime(dt.now(), '%Y%B%d_%H_%M_%ms')

    class MyStreamListener_v4(tweepy.Stream):
        """
        Utility class for v4 tweepy extending Stream class
        """

        def on_data(self, data, track=Tracker):
            with open(Tracker + '_' + time_obj_str + ".json", "a") as file:
                payload = data.decode('utf-8')
                file.write(payload + '\n')
                print(payload + '\n')

        def on_error(self, status_code):
            if status_code == 420:
                # returning False in on_data disconnects the stream
                return False

        def write_data(self, data):
            """This method reads in tweet data as Json and extracts the data we want."""
            try:
                raw_data = json.loads(data)

                if 'text' in raw_data:
                    tweet_id = raw_data['id']
                    username = raw_data['user']['screen_name']
                    created_at = parser.parse(raw_data['created_at'])
                    tweet_text = raw_data['text']
                    hashtags = raw_data['entities']['hashtags']
                    retweet_count = raw_data['retweet_count']
                    source = raw_data['source']
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
                # insert data just collected into MySQL database
                connect(
                    tweet_id,
                    tweet_text,
                    hashtags,
                    source,
                    username,
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
                    location)
                print("Tweet colleted at: {} ".format(str(created_at)))
            except Error as e:
                print(e)

elif tweepy_version == 3:
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)

    time_obj_str = dt.strftime(dt.now(), '%Y%B%d_%H_%M_%ms')
    api = tweepy.API(auth)

    class MyStreamListenerv3(tweepy.StreamListener):
        """
        Utility class for v3 tweepy extending StreamListener class
        """

        def on_data(self, data, track=Tracker):
            """
            - on_data: grab the data and write to disk as json.
            - 'a' mode on open() means that we keep appending to the base of the file and so.
            - This means we could have trailing data when we try to read this json file
            """
            with open(Tracker + '_' + time_obj_str + ".json", "a", encoding="utf-8") as file:
                file.write(data)
                payload = json.loads(data)
                print(payload['text'])
                print(data)

        def on_error(self, status_code):
            """
            - when there is an error encountered in the stream, it disconnects and will need to be restarted.
            """
            if status_code == 420:
                # returning False in on_data disconnects the stream
                return False

        def write_data(self, data):
            """
            This method reads in tweet data as Json and extracts the data we want.
            """
            try:
                raw_data = json.loads(data)

                if 'text' in raw_data:
                    tweet_id = raw_data['id']
                    username = raw_data['user']['screen_name']
                    created_at = parser.parse(raw_data['created_at'])
                    tweet_text = raw_data['text']
                    hashtags = raw_data['entities']['hashtags']
                    retweet_count = raw_data['retweet_count']
                    source = raw_data['source']
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

                    # insert data just collected into MySQL database
                    connect(tweet_id, tweet_text, hashtags, source, username, followers_count, friends_count, listed_count,
                            favourites_count, statuses_count, following, follow_request_sent, notifications, coordinates, place, location)
                    print("Tweet colleted at: {} ".format(str(created_at)))
            except Error as e:
                print(e)

else:
    print(
        f"This utility supports on tweepy versions 3 and 4. You have version {tweepy_version}.c\nUpgrade to 3 or 4")
    raise SystemExit


# Determine tweepy version to work with
if tweepy_version == 4:
    print(f"We are working with Tweepy version {tweepy_version}")
    listen = MyStreamListener_v4(
        consumer_key, consumer_secret, access_token, access_token_secret)

    # We can add more items to the tracker array to listen to more topics
    listen.filter(track=[Tracker])
elif tweepy_version == 3:
    listen = MyStreamListenerv3()
    myStream = tweepy.Stream(auth=api.auth, listener=listen)

    # We can add more items to the tracker array to listen to more topics
    myStream.filter(track=[Tracker])
