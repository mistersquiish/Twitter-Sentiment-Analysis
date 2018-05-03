##########################################################
# File name: sentiment_analysis_module                   #
# Author: Henry Vuong                                    #
# Date Modified: 4/28/2018                               #
# Description: Module used to perform sentiment analysis #
##########################################################

from statistics import mode

import pickle
from nltk.classify import ClassifierI


# class produces a classifier that is an aggregate of the uploaded classifiers
class VoteClassifier(ClassifierI):
    def __init__(self, *classifiers):
        self._classifiers = classifiers

    def classify(self, features):
        votes_prob = []
        for c in self._classifiers:
            vote = c.classify(features)
            dist = c.prob_classify(features)
            prob = abs(dist.prob('neg') - dist.prob('pos'))
            if vote == 'neg':
                prob *= -1
            votes_prob.append(prob)

        vote_prob = 0.00
        for vote in votes_prob:
            vote_prob += vote

        vote_prob /= 2.0

        return vote_prob

    def confidence(self, features):
        votes = []
        for c in self._classifiers:
            v = c.classify(features)
            votes.append(v)
        choice_votes = votes.count(mode(votes))
        conf = choice_votes / len(votes)
        return conf


# open pickled twitter dataset
dataset_file = open("datasets/twitter_dataset.pickle", "rb")
twitterDataset = pickle.load(dataset_file)
dataset_file.close()

# open pickled word features
dataset2_file = open("datasets/words_features.pickle", "rb")
word_features = pickle.load(dataset2_file)
dataset2_file.close()


# function takes only the words in the document that is in word_features
def find_features(document):

    words = set(document)
    features = {}
    for w in word_features:
        features[w] = (w in words)

    return features


# create our list of tuples, labeled either 'pos' or 'neg' with the text in the tweet
featuresets = [(find_features(text), category) for (text, category) in twitterDataset[:15000]]


# pass in text to be compared to featureset that has been generated and classify the sentiment
def sentiment(text):
    feats = find_features(text)

    return voted_classifier.classify(feats)

# load previously saved classifiers


classifier1 = open("classifiers/naive_bayes.pickle", "rb")
NB_classifier = pickle.load(classifier1)
classifier1.close()

classifier2 = open("classifiers/multinomial_naive_bayes.pickle", "rb")
MNB_classifier = pickle.load(classifier2)
classifier2.close()

classifier3 = open("classifiers/bernoulli_naive_bayes.pickle", "rb")
BNB_classifier = pickle.load(classifier3)
classifier3.close()

classifier4 = open("classifiers/linear_support_vector_classification.pickle", "rb")
LinearSVC_classifier = pickle.load(classifier4)
classifier4.close()

classifier5 = open("classifiers/Nu_support_vector_classification.pickle", "rb")
NuSVC_classifier = pickle.load(classifier5)
classifier5.close()

classifier6 = open("classifiers/logistic_regression.pickle", "rb")
LogisticRegression_classifier = pickle.load(classifier6)
classifier6.close()

# create a new classifier from the VoteClassifier class using all our classifiers
voted_classifier = VoteClassifier(MNB_classifier, BNB_classifier)

