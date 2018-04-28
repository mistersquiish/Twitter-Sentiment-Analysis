#####################################################################################
# File name: test_gun_dataset                                                       #
# Author: Henry Vuong                                                               #
# Date Modified: 4/28/2018                                                          #
# Description: script that tests the accuracy of the classifiers to our gun dataset #
#####################################################################################

import sentiment_analysis_module
from nltk.tokenize import word_tokenize
import nltk
import csv
import random

# read in the twitter training dataset
gun_dataset = []
with open('datasets/gun_dataset.csv', 'r') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')

    next(csv_reader)

    for line in csv_reader:
        # positive sentiment
        if line[0] == '1':
            gun_dataset.insert(0, ((list(word_tokenize(line[1]))), 'pos'))
        if line[0] == '0':
            gun_dataset.append(((list(word_tokenize(line[1]))), 'neg'))

# allwords is the list which we will base our sentiment analysis on
allwords = []
allowed_word_types = ["J", "R", "V"]
for (text, category) in gun_dataset:
    pos = nltk.pos_tag(text)
    for w in pos:
        if w[1][0] in allowed_word_types and w[0] != "â™" and w[0] != "«":
            allwords.append(w[0].lower())
allwords = nltk.FreqDist(allwords)

# get the top 5000 words
word_features = list(allwords.keys())[:5000]

# function takes only the words in the document that is in word_features
def find_features(document):

    words = set(document)
    features = {}
    for w in word_features:
        features[w] = (w in words)

    return features

# create our list of tuples, labeled either 'pos' or 'neg' with the text in the tweet
featuresets = [(find_features(text), category) for (text, category) in gun_dataset]


random.shuffle(featuresets)
# training_set = featuresets[:15000]
testing_set = featuresets[:5000]

# print("Original Naive Bayes Algo accuracy:", (nltk.classify.accuracy(sentiment_analysis_module.NB_classifier, testing_set)))
print("MultinomialNB Algo accuracy:", (nltk.classify.accuracy(sentiment_analysis_module.MNB_classifier, testing_set)))
print("BernoulliNB Algo accuracy:", (nltk.classify.accuracy(sentiment_analysis_module.BNB_classifier, testing_set)))
# print("LinearSVC Algo accuracy:", (nltk.classify.accuracy(sentiment_analysis_module.LinearSVC_classifier, testing_set)))
# print("NuSVC Algo accuracy:", (nltk.classify.accuracy(sentiment_analysis_module.NuSVC_classifier, testing_set)))
# print("LogisticRegression Algo accuracy:", (nltk.classify.accuracy(sentiment_analysis_module.LogisticRegression_classifier, testing_set)))