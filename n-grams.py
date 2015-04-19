#!/usr/bin/python2.7

import re
import math
import collections

from optparse import OptionParser

def ngrams(words, n = 2):
	"""
	Creates a list of n-grams where n is the number of words in each tuple.

	:returns:
		List of n-grams.
	"""
	return [tuple(words[i:i+n]) for i in range(0, len(words) - (n - 1))]

nGramNames = ['word', 'bigram', 'trigram', 'fourgram']
def getDescription(n, count):
	"""
	Gets a nice description of the n-gram operation.

	:returns:
		String name.
	"""
	nGramName = nGramNames[n-1] if len(nGramNames) >= n else "%i-gram" % n
	print "Top %i %ss:\n" % (count, nGramName) if count > 1 else "Top %s:\n" % nGramName

def getScoreboard(ngramCounts):
	"""
	Prints a nicely formatted scoreboard of the results.
	"""
	for i, ngramCount in enumerate(ngramCounts):
		print "%s %s %i" % (("%i." % (i + 1)).ljust(2 + int(math.log10(len(ngramCounts)))), ' '.join(ngramCount[0]).ljust(50), ngramCount[1])

def main():
	# Get the command line arguments
	parser = OptionParser()
	parser.add_option("-f", "--file", type = str, dest = "filePath", default = "text.txt", help = "file to read corpus from", metavar = "FILE")
	parser.add_option("-n", type = int, dest = "n", default = 2, help = "number of grams")
	parser.add_option("-t", "--topX", type = int, dest = "topX", default = 10, help = "number of top n-grams to display")
	args = parser.parse_args()[0]

	# Compile a regex to remove superfluous characters
	charactersToDiscard = re.compile(r'[()-;:.\'?!$%"\[\]#0-9]')

	# Get the list of words from the file provided with words lowered and newlines removed
	words = []
	with open(args.filePath, 'r') as fileHandle:
		for line in fileHandle:
			words.extend([word for word in charactersToDiscard.sub("", line).lower().replace('\n', ' ').split(' ') if word != ''])

	# Print the most common n-grams
	getDescription(args.n, args.topX)
	getScoreboard(collections.Counter(ngrams(words, args.n)).most_common(args.topX))

if __name__ == '__main__':
	main()
