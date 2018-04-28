###################################################################################
# File name: generate_classifiers                                                 #
# Author: Henry Vuong                                                             #
# Date Modified: 4/28/2018                                                        #
# Description: script that generates various classifiers from the Twitter dataset #
###################################################################################

import csv
import random

import pickle
import nltk
from nltk.tokenize import word_tokenize
from nltk.classify.scikitlearn import  SklearnClassifier
from sklearn.naive_bayes import MultinomialNB, BernoulliNB
from sklearn.linear_model import LogisticRegression
from sklearn.svm import LinearSVC, NuSVC

# count to limit the dataset to 5000 positive and 5000 negative
countP = 0
countN = 0
# read in the twitter training dataset
twitterDataset = []
with open('datasets/twitter_dataset.csv', 'r') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')

    next(csv_reader)

    for line in csv_reader:
        # positive sentiment
        if line[1] == '1' and countP < 10100:
            twitterDataset.insert(0, ((list(word_tokenize(line[3]))), 'pos'))
            countP += 1
        if line[1] == '0' and countN < 10100:
            twitterDataset.append(((list(word_tokenize(line[3]))), 'neg'))
            countN += 1
    print("Done parsing twitter dataset")

# pickle the twitter dataset for future training
file = open("twitter_dataset","wb")
pickle.dump(twitterDataset, file)


# allwords is the list which we will base our sentiment analysis on
allwords = []
allowed_word_types = ["J", "R", "V"]
for (text, category) in twitterDataset:
    pos = nltk.pos_tag(text)
    for w in pos:
        if w[1][0] in allowed_word_types and w[0] != "â™" and w[0] != "«" and w[0] != "musicmonday" and w[0] != "followfriday":
            allwords.append(w[0].lower())
allwords = nltk.FreqDist(allwords)

# get the top 5000 words
word_features = list(allwords.keys())[:3000]

# pickle the words feature list for future use
file2 = open("datasets/words_features.pickle","wb")
pickle.dump(word_features, file2)
print("Done pickling word_features")

# function takes only the words in the document that is in word_features
def find_features(document):

    words = set(document)
    features = {}
    for w in word_features:
        features[w] = (w in words)

    return features

# create our list of tuples, labeled either 'pos' or 'neg' with the text in the tweet
featuresets = [(find_features(text), category) for (text, category) in twitterDataset[:15000]]

random.shuffle(featuresets)
training_set = featuresets[:12000]
testing_set = featuresets[:5000]
print("Done with generating training_set and testing_set")

# pickle classifiers for easier use in the future
NB_classifier = nltk.NaiveBayesClassifier.train(training_set)
save_classifier1 = open("classifiers/naive_bayes.pickle","wb")
pickle.dump(NB_classifier, save_classifier1)
save_classifier1.close()
print("Done training and pickling NB_classifier")

MNB_classifier = SklearnClassifier(MultinomialNB()).train(training_set)
save_classifier2 = open("classifiers/multinomial_naive_bayes.pickle","wb")
pickle.dump(MNB_classifier, save_classifier2)
save_classifier2.close()
print("Done training and pickling MNB_classifier")

BNB_classifier = SklearnClassifier(BernoulliNB()).train(training_set)
save_classifier3 = open("classifiers/bernoulli_naive_bayes.pickle","wb")
pickle.dump(BNB_classifier, save_classifier3)
save_classifier3.close()
print("Done training and pickling BNB_classifier")

LinearSVC_classifier = SklearnClassifier(LinearSVC()).train(training_set)
save_classifier4 = open("classifiers/linear_support_vector_classification.pickle","wb")
pickle.dump(LinearSVC_classifier, save_classifier4)
save_classifier4.close()
print("Done training and pickling LinearSVC_classifier")

NuSVC_classifier = SklearnClassifier(NuSVC()).train(training_set)
save_classifier5 = open("classifiers/Nu_support_vector_classification.pickle","wb")
pickle.dump(NuSVC_classifier, save_classifier5)
save_classifier5.close()
print("Done training and pickling NuSVC_classifier")

LogisticRegression_classifier = SklearnClassifier(LogisticRegression()).train(training_set)
save_classifier6 = open("classifiers/logistic_regression.pickle","wb")
pickle.dump(LogisticRegression_classifier, save_classifier6)
save_classifier6.close()
print("Done training and pickling LogisticRegression_classifier")