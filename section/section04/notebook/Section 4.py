# -*- coding: utf-8 -*-
# <nbformat>3.0</nbformat>

# <markdowncell>

# # Ling x44 Week 4
# 
# _You can find this notebook on my GitHub repo: http://github.com/obnorthrup/144coursework _  
# _Don't let me start until you're set up!_
# 
# ## Today's project
# 
# We're going to load several text files, get word frequencies, filter common words out, and print some frequency results to a new file.

# <markdowncell>

# ## Part 1: Loading, tokenizing
# 
# Let's load some text files and make a dictionary of word frequencies from them. What are the steps?

# <markdowncell>

# We'll need to:
# 
# 1. Write a function that breaks a text file into a list of words - tokenizeFile()
#     1. Load the file
#     2. Go through line by line and find the words
#     3. Append those words to a list
#     4. Return the list
# 2. Write a function that runs tokenizeFile() on every text file in it - tokenizeDir()
#     1. Find out what's in the directory
#     2. Limit ourselves to just text files (.txt)
#     3. Call tokenizeFiles on each text file and glom all the results together

# <markdowncell>

# ### 1.1 tokenizeFile()
# 
# Let's start small. Load a file into f and print it line-by-line.

# <codecell>

path = "../data/grimm_snippet.txt"
f = open(path, "r")

# One solution:
#curLi = f.readline()
#while curLi != '':
#    print curLi
#    curLi = f.readline()

# Easier for our purposes:
#for line in f:
#    print line

def tokenizer(path): #This function is responsible for tokenizing the text in the provided file.
    f = open(path, "r")
    words = []
    for line in f: #For each line in the loaded file:
        words_only = re.findall(r"[A-Za-z']+", line.lower()) #Strip the punctuation with regular expressions from the text.
        words.extend(words_only)
    return words    
    
print tokenizer(path)

# <markdowncell>

# Ok, now let's find all the words in a string, using a regular expression.

# <codecell>

import re
silly = '''"I should be very silly," said he, "if I went to that shabby
house, and left this charming place;" so he went into the smart house,
and ate and drank at his ease, and forgot the bird, and his country too.'''

silly_list = re.findall(r"[A-z']+", silly.lower())
print silly_list

# <markdowncell>

# Putting these together...

# <codecell>

import re

def tokenizeFile(path):
    f = open(path, "r")

    words = []

    for line in f:
        line_words = re.findall(r"[A-z']+", line.lower())
        words.extend(line_words)
    return words

print tokenizeFile(path)

# <markdowncell>

# ### 1.2 tokenizeDir()
# 
# Ok, now let's call this on multiple files. We'll 1) create a list of paths to text files in a particular directory and 2) loop through that list, running tokenizeFile() as we go.
# 
# First up: List the text files in a directory

# <codecell>

import os

#os.chdir("/Users/obn/Dropbox/Linguistics/Comp Methods/144coursework/Section prep/Section 4/notebook")

print os.getcwd()
os.chdir("..")
print os.getcwd()
print os.listdir(os.getcwd())
print type(os.listdir(os.getcwd()))

theDir = os.listdir(os.getcwd())
for theFile in theDir:
    if theFile.endswith(".md"):
        print "Found one! It's " + theFile

# <markdowncell>

# Now, make a function called txtInDir(directory) that takes a path and returns a list of all the text files in it

# <codecell>

import os

# Your directory will be different
os.chdir("/Users/obn/Dropbox/Linguistics/Comp Methods/144coursework/section/Section 4/notebook")


def txtInDir(directory):
    paths = []
    for theFile in os.listdir(directory):
        if theFile.endswith(".txt"):
            filePath = directory + theFile
            paths.append(filePath)
    return paths

chronoDir = "../data/chronoguide/"
chronoPaths = txtInDir(chronoDir)
print chronoPaths

# <markdowncell>

# Almost there. We have a way to list text files and a way to tokenize a single text file. Write tokenizeDir(directory) to put these together.

# <codecell>

#import re

def tokenizeDir(directory):
    totalWords = []
    pathList = txtInDir(directory)
    #print pathList
    for path in pathList:
        fileWords = tokenizeFile(path)
        totalWords.extend(fileWords)
    return totalWords

chronoWords = tokenizeDir(chronoDir)
print chronoWords[1895:2050]
#print tokenizeFile("../data/chronoguide/chrono_trigger_1.txt")

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
    for word in wordList:
        if word in frequencies:
            frequencies[word] += 1
        else:
            frequencies[word] = 1
    return frequencies

chronoFreq = words2freq(chronoWords)
print chronoFreq

# <markdowncell>

# The main characters in this game are **Crono**, **Marle**, **Lucca**, **Frog**, **Robo**, and **Magus**. Let's see how often they're mentioned.

# <codecell>

heroes = ['crono','marle','lucca','frog','robo','ayla','magus']
for hero in heroes:
    print "{name}: {count} mentions".format(name=hero.capitalize(),count=chronoFreq[hero])

# <markdowncell>

# More generally, let's see what the 30 most frequent words are. What will we have to do?
# 
# 1. Get the dictionary items as a list (so we can sort it)
# 2. Sort the list by values
# 3. Print the 30 largest items

# <codecell>

def freq_dict_to_list(frequencies):
    freq_list = frequencies.items()

    def getCounts(item):
        return item[1]

    freq_list.sort(key= getCounts, reverse= True)
    return freq_list

    # More compact:
    #return sorted(frequencies.items(),key=lambda x:x[1],reverse=True)
    
print freq_dict_to_list(chronoFreq)[:30]

# <markdowncell>

# Let's make this look a little nicer by putting a wrapper on it called top30() that takes a frequency dictionary

# <codecell>

def top30(freqDict):
    freqList = freq_dict_to_list(freqDict)
    for i in range(0,30):
        print "{rank}) {word}: {count}".format(rank=i+1,word=freq_list[i][0],count=freq_list[i][1])
    return None

top30(chronoFreq)

# <markdowncell>

# Hmm, not super useful, given all the common words mixed in. Let's filter the 100 most common English words. (http://en.wikipedia.org/wiki/Most_common_words_in_English)
# 
# 1. Load the common words into a list
# 2. Create a function that takes a frequency dictionary and a list, and returns a dictionary with the items listed removed
# 3. Print top30() on the new dict

# <codecell>

commonList = tokenizeFile("../data/100_most_common.txt")

# <codecell>

def filterFreq(freqDict, filterList):
    filteredFreq = {}
    #common_cust = ['is','are','were']
    for word in freqDict:
            if word not in filterList: # and word not in common_cust:
                filteredFreq[word] = freqDict[word]
    return filteredFreq

filteredChronoFreq = filterFreq(chronoFreq, commonList)

# <codecell>

top30(filteredChronoFreq)

# <markdowncell>

# ## Writing to files
# 
# Let's quickly save the results of `top30()` to a new file in the working directory.

# <codecell>

f = open("top30.txt","w")
#f.write(top30(filteredChronoFreq)) #Fails! Can only write a string.
f.close()

# <markdowncell>

# We need a different version of `top30()`. Let's have it write to a new file, tab delimited. (How might we do this in a better way than I have below?)

# <codecell>

# We need a new version of top30()
def top30tabbed(freqDict):
    freqList = freq_dict_to_list(freqDict)
    output = ''''''
    for i in range(0,30):
        output += str(i+1) + "\t" + freq_list[i][0] + "\t" + str(freq_list[i][1]) + "\n"
    return output

# <codecell>

f = open("top30.txt","w")
f.write(top30string(filteredChronoFreq))
f.close()

# <codecell>


