####################################################################################
# File name: parse_twitter_stream                                                  #
# Author: Henry Vuong                                                              #
# Date Modified: 4/28/2018                                                         #
# Description: parses the twitter_stream_data for locations and save to a csv file #
####################################################################################

import csv
from nltk.tokenize import word_tokenize

statesAbr = ['al', 'ak', 'az', 'ar', 'ca', 'co', 'ct', 'de', 'fl', 'ga',
          'hi', 'id', 'il', 'in', 'ia', 'ks', 'ky', 'la', 'me', 'md', 'ma',
          'mi', 'mn', 'ms', 'mo', 'mt', 'ne', 'nv', 'nh', 'nj', 'nm', 'ny',
          'nc', 'nd', 'oh', 'ok', 'or', 'pa', 'ri', 'sc', 'sd', 'tn', 'tx',
          'ut', 'vt', 'va', 'wa', 'wv', 'wi', 'wy']

statesFull = ['alabama', 'alaska',
          'arizona', 'arkansas', 'california', 'colorado', 'connecticut',
          'delaware', 'florida', 'georgia', 'hawaii', 'idaho', 'illinois',
          'indiana', 'iowa', 'kansas', 'kentucky', 'louisiana', 'maine', 'maryland',
          'massachusetts', 'michigan', 'minnesota', 'mississippi', 'missouri', 'montana',
          'nebraska', 'nevada', 'new hampshire', 'new jersey', 'new mexico', 'new york',
          'north carolina', 'north dakota', 'ohio', 'oklahoma', 'oregon', 'pennsylvania',
          'rhode island', 'south  carolina', 'south dakota', 'tennessee', 'texas', 'utah',
          'vermont', 'virginia', 'washington', 'west virginia', 'wisconsin', 'wyoming']

with open('datasets/twitter_stream_data_parsed.csv', 'w', newline='') as csvfile:
    field_names = ['Tweet Text', 'Location', 'Sentiment Polarity']
    writer = csv.writer(csvfile)
    writer.writerow(field_names)
    with open('datasets/twitter_stream_data.csv', 'r') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')

        next(csv_reader)

        tweet_count = 0
        for line in csv_reader:
            words = word_tokenize(line[1])
            if len(words) != 0:
                done = False
                for state in statesAbr:
                    if state in [word.lower() for word in words]:
                        writer.writerow([line[0], state, line[2]])
                        done = True

                if not done:
                    for state in statesFull:
                        if state in [word.lower() for word in words]:
                            writer.writerow([line[0], statesAbr[statesFull.index(state)], line[2]])
