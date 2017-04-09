# -*- coding: utf-8 -*-

import sys
from process_tweets import *
from train import *
from get_tweets import *

if __name__ == '__main__':
    # files = os.listdir(sys.argv[1])
    state = str(sys.argv[1])
    filename = open("tweets_"+state+".txt",'r')
    users = {}

    liberal = {}
    conservative = {}
    lib = open('liberal.txt', 'r')
    con = open('conservative.txt', 'r')

    liberal = get_freqs(lib, liberal)
    conservative = get_freqs(con, conservative)

    # Get distinct words
    vocab = []
    for word in liberal:
        if word not in vocab:
            vocab.append(word)

    for word in conservative:
        if word not in vocab:
            vocab.append(word)

    total_vocab = len(vocab)

    liberal, conservative, total_vocab = get_probs(liberal, conservative, total_vocab)

    user_results = testNaiveBayes(filename, total_vocab, liberal, conservative)

    compareResults(user_results, state)
    # for line in file:
    #     username, tweet = line.split(',',1)
    #     tweet = preprocess(tweet)

    #     # testNaiveBayes: take preprocessed tokens of 1 tweet,
    #     # return the result of classification

    #     # take result == conservative as 1, liberal as -1
    #     if username in users:
    #         users[username] = users[username] + result

    # NumConservative = 0
    # NumLiberal = 0
    # for user in users:
    #     if users[user] > 0:
    #         NumConservative += 1
    #     elif users[user] < 0:
    #         NumLiberal += 1

    #ConservativePercentage = NumConservative/(NumLiberal+NumConservative)
    #LiberalPercentage = NumLiberal/(NumLiberal+NumConservative)

    #print ("Conservative: "+str(ConservativePercentage))
    #print ("Liberal: "+str(LiberalPercentage))