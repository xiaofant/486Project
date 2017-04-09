# -*- coding: utf-8 -*-

import sys
from process_tweets import *
from train import *
from get_tweets import *

if __name__ == '__main__':
    # files = os.listdir(sys.argv[1])
    state = sys.argv[1]
    file = open("486Project/tweets_"+state+".txt",'r')
    users = {}
    for line in file:
        username, tweet = line.split(',',1)
        tweet = preprocess(tweet)

        # testNaiveBayes: take preprocessed tokens of 1 tweet,
        # return the result of classification

        # take result == conservative as 1, liberal as -1
        if username in users:
            users[username] = users[username] + result

    NumConservative = 0
    NumLiberal = 0
    for user in users:
        if users[user] > 0:
            NumConservative += 1
        elif users[user] < 0:
            NumLiberal += 1

    ConservativePercentage = NumConservative/(NumLiberal+NumConservative)
    LiberalPercentage = NumLiberal/(NumLiberal+NumConservative)

    print ("Conservative: "+str(ConservativePercentage))
    print ("Liberal: "+str(LiberalPercentage))