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



	return liberal, conservative



def main():
	liberal = {}
	conservative = {}
	lib = open('liberal.txt', 'r')
	con = open('conservative.txt', 'r')

	liberal = get_freqs(lib, liberal)
	conservative = get_freqs(con, conservative)

	total_vocab = len(liberal.keys()) + len(conservative.keys())

	liberal, conservative = get_probs(liberal, conservative, total_vocab)

	print liberal
	print "=================================="
	print conservative
	return liberal, conservative






if __name__ == "__main__":
    main()













