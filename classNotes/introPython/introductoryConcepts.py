#!/usr/bin/env python

__author__ = 'panand'
__email__ = "panand@ucsc.edu"
__credits__ = []

import urllib2
import BeautifulSoup
from collections import Counter

url1 = "http://www.gutenberg.org/cache/epub/17268/pg17268.txt"

def getText(url):
	"""
	pulls the contents of url1, loads it in a text file.

    Args:
		url: location online [string]

    Returns:
        text: the text at that URL [string]

    Raises:
        Nothing

	"""
	c = urllib2.urlopen(url1)
	text = c.read()
	return text

def main():
	"""
	creates a frequency wordlist for url1
		1. calls getText to extract the text from the url
		2. replaces newlines with spaces
		3. separates punctuation from words
		4. normalizes word case to lower case
		5. constructs wordlist Counter

    Args:
		None

    Returns:
        frequencies: a frequency list (Counter)

    Raises:
        Nothing

	"""
	c = urllib2.urlopen(url1)
	text = c.read()
	normedText = text.replace("\r\n", " ")

	punctuation = [';', ',', '.', "'", '"', "_"]

	for p in punctuation:
		normedText = normedText.replace(p, " " + p + " ")

	normedText = normedText.replace("  ", " ")

	tokens = normedText.split(" ")
	frequencies = Counter()
	for token in tokens:
		if token != "":
			normedtoken = token.lower()
			frequencies[normedtoken] += 1
	frequencies.most_common(30)

def testSoup():
	url = "http://www.gutenberg.org/ebooks/17268"

	c = urllib2.urlopen(url)
	s = BeautifulSoup(c.read())

if __name__ == "__main__":
	main()
