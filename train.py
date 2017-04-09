import os
import glob

##########################
# THIS ASSUMES THAT THE TWEETS HAVE ALREADY BEEN PROCESSED AND
# HAVE BEEN WRITTEN TO A FILE
##########################

def get_freqs(file, dictionary):
	for line in file:
		for word in line.split(' '):
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
	with open(filename, 'r') as f:
		for line in f:
			username, tweet = line.split(',')
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
			# liberal_users = []
			# conserv_users = []

			if conserv_calc > liberal_calc:
				user_results[username] = 'conservative'
			else:
				user_results[username] = 'liberal'

	# Returns dictionary with key: username, value: classification
	return user_results

def calculateAccuracy(user_results, state):

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
    "NV": "D",
    "NH": "D",
    "NJ": "D", 
    "NM": "D",
    "NY": "D",
    "NC": "R",
    "ND": "R",
    "OH": "R",
    "OK": "R",
    "OR": "D",
    "PA": "R",
    "RI": "D",
    "SC": "R", 
    "SD": "R",
    "TN": "R",
    "TX": "R",
    "UT": "R",
    "VT": "D",
    "VA": "D",
    "WA": "D",
    "WV": "R",
    "WI": "R",
    "WY": "R"}

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
    print 'Expected outcome is: ' + vote_results[state]
    print 'Actual outcome is: ' + expected

def main():
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

	print liberal
	print "=================================="
	print conservative
	return liberal, conservative






if __name__ == "__main__":
    main()













