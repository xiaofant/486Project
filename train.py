# -*- coding: utf-8 -*-

import os
import glob
import math
from process_tweets import *
from get_follower_id import *
from friendship import *

##########################
# THIS ASSUMES THAT THE TWEETS HAVE ALREADY BEEN PROCESSED AND
# HAVE BEEN WRITTEN TO A FILE
##########################

def get_freqs(file, dictionary):
	for line in file:
		line = preprocess(line)
		line = removeStopwords(line)
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

def followingCalculations(username):
	# Liberal and conservative users on Twitter
	liberal_users = ['HillaryClinton', 'BarackObama', 'JoeBiden', 'SenSanders', \
						'BernieSanders', 'MichelleObama', 'timkaine', 'BuzzFeed', \
						'BuzzFeedNews', 'Politico', 'washingtonpost', 'nytimes', 'MSNBC', \
						'billmaher', 'TheDailyShow', 'MartinBashir', 'MikeBloomberg', 'iamjohnoliver', \
						'Trevornoah']
	conserv_users = ['realDonalTrump', 'mike_pence', 'tedcruz', 'SpeakerRyan', 'PRyan', \
						'SenJohnMccain', 'FoxNews', 'theblaze', 'YoungCons', 'DRUDGE_REPORT', \
						'BreitbartNews', 'rushlimbaugh', 'seanhannity', 'ASavageNation', 'glennbeck', \
						'hughhewitt', 'marklevinshow', 'TomiLahren', 'PrisonPlanet']


	#print 'getting follower info'
	liberal_user_id = get_user_ids(liberal_users)
	conserv_user_id = get_user_ids(conserv_users)

	follower_values = 0
	# Liberal = positive (+1)
	# Conservative = negative (-1)

	#print 'getting users followers'
	username_followers = following_users(username)

	#print 'done getting all followers'
	# Check if user follows liberal/conservative people
	for user in liberal_user_id:
		if user in username_followers:
			follower_values += 1

	for user in conserv_user_id:
		if user in username_followers:
			follower_values -= 1

	return follower_values

def testNaiveBayes(filename, total_vocab, liberal, conservative):
	user_results = {}
	tweets = []
	borderline = 0

	for line in filename:
		line = line.split(', ')
		username = line[0]
		tweet = preprocess(line[1].decode('utf-8'))
		tweet = removeStopwords(tweet)

		# Don't pull duplicate tweets from test data
		if tweet in tweets:
			continue
		else:
			tweets.append(tweet)

		conserv_calc = math.log10(0.5)
		liberal_calc = math.log10(0.5)

		hillaryHashtag = False
		trumpHashtag = False
		hillaryHashtagCount = 0
		trumpHashtagCount = 0
		liberalHashtags = ['imwithher', 'hillarywon', 'iamwithher', 'votehillary', 'presidentclinton', 'clinton2016', 'hillaryclinton', 'nevertrump', 'basketofdeplorables']
		conservHashtags = ['maga', 'trumpwon', 'votetrump', 'presidenttrump', 'trump2016', 'neverhillary', 'donaldtrump', 'makeamericagreatagain', 'crookedhillary', 'lockherup']

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

			if word in liberalHashtags:
				hillaryHashtag = True
				hillaryHashtagCount += 1
			if word in conservHashtags:
				trumpHashtag = True
				trumpHashtagCount += 1

		
		#print follwing_calc
		#print conserv_calc
		#print liberal_calc
		#break

		if username not in user_results:
			user_results[username] = 0

		# *** RATE LIMIT ERROR FROM TWITTER -- UNABLE TO USE IN CALCULATIONS ***
		# following_calc = followingCalculations(username)
		# # Add followers metric
		# if following_calc > 0:
		# 	user_results[username] += 1
		# elif following_calc < 0:
		# 	user_results[username] -= 1

		# Hashtag calculations included
		if trumpHashtag:
			# trump and hillary
			if hillaryHashtag:
				if trumpHashtagCount > hillaryHashtagCount:
					user_results[username] -=1
				elif hillaryHashtagCount > trumpHashtagCount:
					user_results[username] += 1
			# only trump
			else:
				user_results[username] -=1
		elif hillaryHashtag:
			user_results[username] += 1


		# give precedence to naive bayes
		if conserv_calc > liberal_calc:
			user_results[username] -= 1
			if user_results[username] == 0:
				user_results[username] = -1


		else:
			user_results[username] += 1
			if user_results[username] == 0:
				user_results[username] = 1
				

	# Returns dictionary with key: username, value: classification
	#print (user_results)
	return user_results

def compareResults(user_results, state):

	vote_results = {
	"AL": ["R", 62.9, 34.6],
	"AK": ["R", 52.9, 37.7],
	"AZ": ["R", 49.5, 45.4],
	"AR": ["R", 60.4, 33.8],
	"CA": ["D", 32.8, 61.6],
	"CO": ["D", 44.4, 47.2],
	"CT": ["D", 41.2, 54.5],
	"DC": ["D", 4.1, 92.8],
	"DE": ["D", 41.9, 53.4],
	"FL": ["R", 49.1, 47.8],
	"GA": ["R", 51.3, 45.6], 
	"HI": ["D", 30.1, 62.3],
	"ID": ["R", 59.2, 27.6],
	"IL": ["D", 39.4, 55.4],
	"IN": ["R", 57.2, 37.9],
	"IA": ["R", 51.8, 42.2],
	"KS": ["R", 57.2, 36.2],
	"KY": ["R", 62.5, 32.7],
	"LA": ["R", 58.1, 38.4],
	"ME": ["D", 45.2, 47.9],
	"MD": ["D", 35.3, 60.5], 
	"MA": ["D", 33.5, 60.8],
	"MI": ["R", 47.6, 47.3],
	"MN": ["D", 45.4, 46.9],
	"MS": ["R", 58.3, 39.7],
	"MO": ["R", 57.1, 38.0],
	"MT": ["R", 56.5, 36.0],
	"NE": ["R", 60.3, 34.0],
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
		if vote < 0:
			conservative_count += 1
		elif vote > 0:
			liberal_count += 1

	expected = ''

	if conservative_count > liberal_count:
		expected = 'R'
	else:
		expected = 'D'

	#print "c count: " + str(conservative_count)
	#rint "l count: " + str(liberal_count)
	conserv_percent = float(float(conservative_count) / (len(user_results))) * 100
	liberal_percent = float(float(liberal_count) / (len(user_results))) * 100
	print 'Expected outcome for ' + state + ' is: ' + vote_results[state][0] + ' (R: ' + str(vote_results[state][1]) + '%, D: ' + str(vote_results[state][2]) + '%)'
	print 'Actual outcome for ' + state + ' is: ' + expected + ' (R: ' + str(round(conserv_percent,1)) + '%, D: ' + str(round(liberal_percent,1)) + '%)'

	# For accuracy, return 1 if correctly predicted, return 0 if not
	if expected == vote_results[state][0]:
		return 1
	else:
		return 0










