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

			# Determine whether document is more of a lie or truth
			if conserv_calc > liberal_calc:
				#print filename, 'lie'
				return 'conservative'
			else:
				#print filename, 'truth'
				return 'liberal'


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













