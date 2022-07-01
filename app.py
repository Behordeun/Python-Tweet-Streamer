import mysql.connector
from mysql.connector import Error
import tweepy
import json
from dateutil import parser
import time
import os
import subprocess
from keys import consumer_key, consumer_secret, access_token, access_token_secret, host, password, database, user, charset

# importing file which sets env variable
#subprocess.call("./settings.sh", shell = True)

consumer_key = consumer_key
consumer_secret = consumer_secret
access_token = access_token
access_token_secret = access_token_secret
password = password


def connect(
        created_at,
        tweet_id,
        tweet_text,
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
            query = "INSERT INTO elections_db (created_at, tweet_id, tweet_text, source, username, retweet_count, followers_count, friends_count, listed_count, favourites_count, statuses_count, following, follow_request_sent, notifications, coordinates, place, location) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
            cursor.execute(query, (
                created_at,
                tweet_id,
                tweet_text,
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
                location))
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

    def on_data(self, data):
        """This method reads in tweet data as Json and extracts the data we want."""
        try:
            raw_data = json.loads(data)

            if 'text' in raw_data:
                created_at = parser.parse(raw_data['created_at'])
                tweet_id = raw_data['id']
                tweet_text = raw_data['text']
                source = raw_data['source']
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
                # insert data just collected into MySQL database
                connect(
                    created_at,
                    tweet_id,
                    tweet_text,
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
                    location)
                print("Tweet colleted at: {} ".format(str(created_at)))
        except Error as e:
            print(e)


if __name__ == '__main__':

    # # #Allow user input
    # track = []
    # while True:

    # 	input1  = input("what do you want to collect tweets on?: ")
    # 	track.append(input1)

    # 	input2 = input("Do you wish to enter another word? y/n ")
    # 	if input2 == 'n' or input2 == 'N':
    # 		break

    # print("You want to search for {}".format(track))
    # print("Initialising Connection to Twitter API....")
    # time.sleep(2)

    # authentification so we can access twitter
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

    listener.filter(track=track)#, languages=['en'])
