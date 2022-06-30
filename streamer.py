# -*- coding: utf-8 -*-
"""
Created on Tue Jun 19 11:18:37 2018
Latest Update on Sun Jun 26 2022

Updated to support tweepy v4 and continue supporting v3 on Thursday June 6 16:33 WAT
Updated to fix multiple file creation bug on Sunda June 26 2022

@author: Behordeun
"""
###################################################################################
##1. This Script will capture and save to file, a stream of tweets according to the keyword(s) input by the user.
##2. The file is saved as a "keyword.json"
##3. If this script is run more than once with the same keyword, the initial file saved with the keyword will be incremented
##4. Script will run till and error is encountered in the stream or it is stopped with "Ctrl+C" twice.
##################################################################################

import tweepy
from datetime import datetime as dt
import pandas as pd
from datetime import datetime as dt
from keys import access_token, access_token_secret, consumer_key, consumer_secret


Tracker=input('What are we tracking on Twitter?: ')

try:
    tweepy_version = int(tweepy.__version__[0])
except Exception as e:
    print(f"Error while determining the version of tweepy you are working with.\nDetails => {e} ")

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
                #returning False in on_data disconnects the stream
                return False

elif tweepy_version == 3:
    auth =  tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token,access_token_secret)

    time_obj_str = dt.strftime(dt.now(), '%Y%B%d_%H_%M_%ms')
    api=tweepy.API(auth)

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
            with open(Tracker + '_' + time_obj_str + ".json", "a",encoding="utf-8") as file:
                file.write(data)
                # payload = json.loads(data)
                # print(payload['text'])
                print(data)

        def on_error(self, status_code):
            """
            - when there is an error encountered in the stream, it disconnects and will need to be restarted.
            """
            if status_code == 420:
                #returning False in on_data disconnects the stream
                return False
else:
    print(f"This utility supports on tweepy versions 3 and 4. You have version {tweepy_version}.c\nUpgrade to 3 or 4")
    raise SystemExit


#Determine tweepy version to work with
if tweepy_version == 4:
    print(f"We are working with Tweepy version {tweepy_version}")
    listen = MyStreamListener_v4(consumer_key, consumer_secret, access_token, access_token_secret)

    #We can add more items to the tracker array to listen to more topics
    listen.filter(track=[Tracker])
elif tweepy_version == 3:
    listen = MyStreamListenerv3()
    myStream = tweepy.Stream(auth = api.auth, listener=listen)

    #We can add more items to the tracker array to listen to more topics
    myStream.filter(track=[Tracker])