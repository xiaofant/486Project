# -*- coding: utf-8 -*-

import sys
from process_tweets import *
from train import *
from get_tweets import *
from friendship import *

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
