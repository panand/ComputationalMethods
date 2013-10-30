# -*- coding: utf-8 -*-
# <nbformat>3.0</nbformat>

# <markdowncell>

# # Ling x44 Week 4
# 
# _You can find this notebook on my GitHub repo: http://github.com/obnorthrup/144coursework _  
# _Don't let me start until you're set up! You'll also need my `data` folder, which is different from the one on the course website._
# 
# ## Today's project
# 
# We're going to load several text files, get word frequencies, filter common words out, and print some frequency results to a new file.

# <markdowncell>

# ## Part 1: Loading, tokenizing
# 
# Let's load some text files and make a dictionary of word frequencies from them. What are the steps?

# <markdowncell>

#  

# <markdowncell>

# ### 1.1 tokenizeFile()
# 
# Let's start small. Load a file (grimm_snippet) and print it line-by-line.

# <codecell>


# <markdowncell>

# Ok, now let's find all the words in a string, using a regular expression.

# <codecell>

import re
silly = '''"I should be very silly," said he, "if I went to that shabby
house, and left this charming place;" so he went into the smart house,
and ate and drank at his ease, and forgot the bird, and his country too.'''


# <markdowncell>

# Putting these together...

# <codecell>

import re

def tokenizeFile(path):
    
    # Your code here
    
    pass

yourPath = ""
print tokenizeFile(yourPath)

# <markdowncell>

# ### 1.2 tokenizeDir()
# 
# Ok, now let's call this on multiple files. We'll 1) create a list of paths to text files in a particular directory and 2) loop through that list, running tokenizeFile() as we go.
# 
# First up: List the text files in a directory

# <codecell>

import os

#os.chdir("/Users/obn/Dropbox/Linguistics/Comp Methods/x44private/Section prep/")

# <markdowncell>

# Now, make a function called txtInDir(directory) that takes a path (to the `chronoguide` directory) and returns a list of all the text files in it

# <codecell>

def txtInDir(directory):
    # Your code here
    pass

#chronoDir = ???
#chronoFileList = txtinDir(chronoDir)
#print chronoFileList

# <markdowncell>

# Almost there. We have a way to list text files and a way to tokenize a single text file. Write tokenizeDir(directory) to put these together.

# <codecell>

#import re

def tokenizeDir(directory):
    
    # Your code here
    pass

#chronoWords = tokenizeDir(chronoDir)
#print words[1895:2050]

# <markdowncell>

# ## Part 2: Frequencies
# 
# Let's make a dictionary of word frequencies from chronoWords. Steps:
# 
# 1. Initialize a dictionary
# 2. Loop through chronoWords
#     1. If a word is in the dictionary, increment its value
#     2. If a word isn't in the dictionary, add it with value 1

# <codecell>

def words2freq(wordList):
    frequencies = {}
    # Your code here. How do we loop through the words in the 'words' list?
    return frequencies

#chronoFreq = words2freq(chronoWords)
#print chronoFreq

# <markdowncell>

# The main characters in this game are **Crono**, **Marle**, **Lucca**, **Frog**, **Robo**, and **Magus**. Let's see how often they're mentioned. Print the results nicely using `.format()`

# <codecell>


# <markdowncell>

# More generally, let's see what the 30 most frequent words are. What will we have to do?

# <markdowncell>

#  

# <codecell>

def freq_dict_to_list(frequencies):
    # Your code here
    pass
    
#print freq_dict_to_list(chronoFreq)[:30]

# <markdowncell>

# Let's make this look a little nicer by putting a wrapper on it called top30() that takes a frequency dictionary

# <codecell>

def top30(freqDict):
    # Your cod here

#top30(chronoFreq)

# <markdowncell>

# Hmm, not super useful, given all the common words mixed in. Let's filter the 100 most common English words. (http://en.wikipedia.org/wiki/Most_common_words_in_English)
# 
# 1. Load the common words into a list
# 2. Create a function that takes a frequency dictionary and a list, and returns a dictionary with the items listed removed
# 3. Print top30() on the new dict

# <codecell>

# Load the common word list file

# <codecell>

def filterFreq(freqDict, filterList):
    # Your code here
    pass

#filteredChronoFreq = filterFreq(chronoFreq, commonList)

# <codecell>

#top30(filteredChronoFreq)

# <markdowncell>

# ## Writing to files
# 
# Let's quickly save the results of `top30()` to a new file in the working directory.

# <codecell>

f = open("top30.txt","w")
#f.write(top30(filteredChronoFreq)) #Fails! Can only write a string.
f.close()

# <codecell>

# We need a new version of top30()
def top30string(freqDict):
    # Your code here
    pass

# <codecell>

f = open("top30.txt","w")
#f.write(top30string(filteredChronoFreq))
f.close()

# <codecell>


