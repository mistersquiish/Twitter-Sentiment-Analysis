#############################################################################
# File name: twitter_stream                                                 #
# Author: Henry Vuong                                                       #
# Date Modified: 4/28/2018                                                  #
# Description: script that collects twitter tweets using Tweepy/Twitter API #
#############################################################################

from tweepy import Stream
from tweepy import OAuthHandler
from tweepy.streaming import StreamListener
import sentiment_analysis_module
import json
import csv

consumerKey = "jH7AHkg7xR5BIce9JQkgJIqwZ"
consumerSecret = "89bDpRvlsWptNL6P1cwy1GrXwtaExE3PRuVXpk0a0yYQXiduDP"
accessToken = "2562821789-Lha1HBpzPQTziFQ6vkJEqpbLjpCd2BYPGohCJCZ"
accessTokenSecret = "TS1y9mTEWd3ckdg9UAKm1mpuf9vsxc9umEpzXzuaPgqcW"

auth = OAuthHandler(consumerKey, consumerSecret)
auth.set_access_token(accessToken, accessTokenSecret)

# class streams tweets and writes the text, location, and sentiment value of the text to a csv file
class listener(StreamListener):
    sentimment_index = 0
    count = 0

    def on_data(self, data):
        all_data = json.loads(data)

        user_data = all_data["user"]

        location = user_data["location"]
        tweet = all_data["text"]
        sentiment_value = sentiment_analysis_module.sentiment(tweet)

        writer.writerow([tweet, location, sentiment_value])

        # just for me to track how many tweets I have saved
        self.count += 1

        if self.count % 100 == 0:
            print(self.count)

        return True

    def on_error(self, status):
        print(status)

searchTerm = "gun"

twitterStream = Stream(auth, listener())
with open('datasets/twitter_stream_data.csv', 'w', newline='') as csvfile:
    field_names = ['Tweet Text', 'Location', 'Sentiment Polarity']
    writer = csv.writer(csvfile)
    writer.writerow(field_names)
    twitterStream.filter(track=[searchTerm])

