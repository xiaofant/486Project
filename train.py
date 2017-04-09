# -*- coding: utf-8 -*-

import os
import glob
import math
from process_tweets import *

##########################
# THIS ASSUMES THAT THE TWEETS HAVE ALREADY BEEN PROCESSED AND
# HAVE BEEN WRITTEN TO A FILE
##########################

def get_freqs(file, dictionary):
	for line in file:
		line = preprocess(line)
		for word in line:
			if word in dictionary:
				dictionary[word] += 1
			else:
				dictionary[word] = 1


	return dictionary

def get_probs(liberal, conservative, total_vocab):
	for word, freq in liberal.iteritems():
		liberal[word] = float(freq + 1) / float(total_vocab + len(liberal.keys()))

	for word, freq in conservative.iteritems():
		conservative[word] = float(freq + 1) / float(total_vocab + len(conservative.keys()))

	return liberal, conservative, total_vocab

def testNaiveBayes(filename, total_vocab, liberal, conservative):
	user_results = {}

	for line in filename:
		line = preprocess(line.decode('utf-8'))
		print line
		username = line[0]
		tweet = line[1:]
		conserv_calc = math.log10(0.5)
		liberal_calc = math.log10(0.5)

		# Calculate conservative and liberal calculations for user via naive bayes
		for word in tweet:
			if word in conservative:
				conserv_calc += math.log10(float(conservative[word]))
				
			else:
				conserv_calc += math.log10(1.00 / float(len(conservative.keys()) + total_vocab))
				
			if word in liberal:
				liberal_calc += math.log10(float(liberal[word]))
			else:
				liberal_calc += math.log10(1.00 / float(len(liberal.keys()) + total_vocab))

		# Add in who the user follows 
		# *** SAM ADD IN THE LIST OF CONSERVATIVE/LIBERAL USERS HERE **** 
		liberal_users = ['@HillaryClinton', '@BarackObama', '@JoeBiden', '@SenSanders', 
							'@BernieSanders', '@MichelleObama', '@timkaine', '@BuzzFeed', \
							'@BuzzFeedNews', '@Politico', '@washingtonpost', '@nytimes', '@MSNBC', \
							'@billmaher', '@TheDailyShow', '@MartinBashir', '@MikeBloomberg', '@iamjohnoliver', \
							'@Trevornoah']
		conserv_users = ['@realDonalTrump', '@mike_pence', '@tedcruz', '@SpeakerRyan', '@PRyan', \
							'@SenJohnMccain', '@FoxNews', '@theblaze', '@YoungCons', '@DRUDGE_REPORT', \
							'@BreitbartNews', '@rushlimbaugh', '@seanhannity', '@ASavageNation', '@glennbeck', \
							'@hughhewitt', '@marklevinshow', '@TomiLahren', '@PrisonPlanet']

		print conserv_calc
		print liberal_calc
		if conserv_calc > liberal_calc:
			user_results[username] = 'conservative'
		else:
			user_results[username] = 'liberal'

	# Returns dictionary with key: username, value: classification
	print (user_results)
	return user_results

def compareResults(user_results, state):

	vote_results = {
	"AL": "R",
	"AK": "R",
	"AZ": "R",
	"AR": "R",
	"CA": "D",
	"CO": "D",
	"CT": "D",
	"DC": "D",
	"DE": "D",
	"FL": "R",
	"GA": "R", 
	"HI": "D",
	"ID": "R",
	"IL": "D",
	"IN": "R",
	"IA": "R",
	"KS": "R",
	"KY": "R",
	"LA": "R",
	"ME": "D",
	"MD": "D", 
	"MA": "D",
	"MI": "R",
	"MN": "D",
	"MS": "R",
	"MO": "R",
	"MT": "R",
	"NE": "R",
	"NV": ["R", 47.9, 46.9],
	"NH": ["D", 47.2, 47.6],
	"NJ": ["D", 41.8, 55.0], 
	"NM": ["D", 40.0, 48.3],
	"NY": ["D", 37.5, 58.8],
	"NC": ["R", 50.5, 46.7],
	"ND": ["R", 64.1, 27.8],
	"OH": ["R", 52.1, 43.5],
	"OK": ["R", 65.3, 28.9],
	"OR": ["D", 41.1, 51.7],
	"PA": ["R", 48.8, 47.6],
	"RI": ["D", 39.8, 55.4],
	"SC": ["R", 54.9, 40.8], 
	"SD": ["R", 61.5, 31.7],
	"TN": ["R", 61.1, 34.9],
	"TX": ["R", 52.6, 43.4],
	"UT": ["R", 45.9, 27.8],
	"VT": ["D", 32.6, 61.1],
	"VA": ["D", 45.0, 49.9],
	"WA": ["D", 38.2, 54.4],
	"WV": ["R", 68.7, 26.5],
	"WI": ["R", 47.9, 46.9],
	"WY": ["R", 70.1, 22.5]}
	
	conservative_count = 0
	liberal_count = 0

	for user, vote in user_results.items():
		if vote == 'conservative':
			conservative_count += 1
		else:
			liberal_count += 1

	expected = ''

	if conservative_count > liberal_count:
		expected = 'R'
	else:
		expected = 'D'

	print "c count: " + str(conservative_count)
	print "l count: " + str(liberal_count)
	conserv_percent = float(float(conservative_count) / (conservative_count + liberal_count)) * 100
	liberal_percent = float(float(liberal_count) / (conservative_count + liberal_count)) * 100
	print 'Expected outcome is: ' + vote_results[state] + '(R: ' + str(conserv_percent) + ', D: ' + str(liberal_percent) + ')'
	print 'Actual outcome is: ' + expected

# def main():
# 	liberal = {}
# 	conservative = {}
# 	lib = open('liberal.txt', 'r')
# 	con = open('conservative.txt', 'r')

# 	liberal = get_freqs(lib, liberal)
# 	conservative = get_freqs(con, conservative)

# 	# Get distinct words
# 	vocab = []
# 	for word in liberal:
# 		if word not in vocab:
# 			vocab.append(word)

# 	for word in conservative:
# 		if word not in vocab:
# 			vocab.append(word)

# 	total_vocab = len(vocab)

# 	liberal, conservative, total_vocab = get_probs(liberal, conservative, total_vocab)

# 	print liberal
# 	print "=================================="
# 	print conservative
# 	return liberal, conservative






if __name__ == "__main__":
	main()













