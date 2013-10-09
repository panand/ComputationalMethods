# -*- coding: utf-8 -*-
# <nbformat>3.0</nbformat>

# <markdowncell>

# # Manipulating strings as lists
# 
# Let's 1) reverse the order of the characters in a string, and 2) reverse each word in a multi-word string. Some scratch space:

# <codecell>


# <codecell>


# <codecell>


# <codecell>


# <codecell>


# <codecell>


# <markdowncell>

# ## Now make it a function

# <codecell>

def reverseString(string):
    """
    Reverses the order of a string
    
    Arguments:
        string (a string) to reverse
    
    Returns:
        reversedStr (a string) that is reversed
        
    Raises:
        nothing
    """
    # Your code here       
    
if __name__ == "__main__":
    print reverseString("testing")

# <markdowncell>

# Let's have it do more than a single word:

# <codecell>

def reverseWords(sentence):
    """
    Reverses each token successively in a sentence (split by space)
    
    Arguments:
        sentence (a string) to split and reverse
    
    Returns:
        a string whole tokens are reversed
        
    Raises:
        nothing
    """

    # Your code here
    
if __name__ == "__main__":
    print "Intended output:"
    print "Eseht era eht semit erehw s'elpoep serutan era detset .ylereves"
    print "Actual output:"
    print reverseWords("These are the times where people's natures are tested severely.")

# <markdowncell>

# # Sorting lists by key functions

# <markdowncell>

# Goal: Sort a list of strings by the position of the first 'e'
# 
# But first, let's just sort alphabetically, reverse alphabetically, and by length

# <codecell>

test = "Eseht era eht semit erehw s'elpoep serutan era detset .ylereves"

# <codecell>


# <codecell>


# <codecell>


# <codecell>


# <markdowncell>

# Ok, now let's make a more complex function to use as the sorting key

# <codecell>

# Sort by the following convention:
# the location of the first 'e' in the sentence

def getFirstInstance(string, substring):
    """
    gets the location of the first substring in a string
    
    Arguments:
        string (a string) to examine
        substring (a string) to look for
    
    Returns:
        the first index of substring
        
    Raises:
        nothing
    """
    # Your code here

def getFirstE(string):
    # your code here

if __name__ == "__main__":
    test = "Eseht era eht semit erehw s'elpoep serutan era detset .ylereves"
    tokens = test.split(" ")
    tokens.sort(key=getFirstE)
    print tokens

# <markdowncell>

# Why use find() vs index()?

# <codecell>


# <markdowncell>

# # Fun with dictionaries
# 
# What does this code do?

# <codecell>

def getMobyDickWords():
    mobydick = """Call me Ishmael. Some years ago -- never mind how long precisely--having
little or no money in my purse, and nothing particular to interest me on
shore, I thought I would sail about a little and see the watery part of
the world. It is a way I have of driving off the spleen and regulating
the circulation. Whenever I find myself growing grim about the mouth;
whenever it is a damp, drizzly November in my soul; whenever I find
myself involuntarily pausing before coffin warehouses, and bringing up
the rear of every funeral I meet; and especially whenever my hypos get
such an upper hand of me, that it requires a strong moral principle to
prevent me from deliberately stepping into the street, and methodically
knocking people's hats off -- then, I account it high time to get to sea
as soon as I can. This is my substitute for pistol and ball. With a
philosophical flourish Cato throws himself upon his sword; I quietly
take to the ship. There is nothing surprising in this. If they but knew
it, almost all men in their degree, some time or other, cherish very
nearly the same feelings towards the ocean with me.

There now is your insular city of the Manhattoes, belted round by
wharves as Indian isles by coral reefs -- commerce surrounds it with
her surf. Right and left, the streets take you waterward. Its extreme
downtown is the battery, where that noble mole is washed by waves, and
cooled by breezes, which a few hours previous were out of sight of land.
Look at the crowds of water-gazers there."""
    normedText = mobydick.replace("\n", " ")
    punctuation = ";:,.?!-"
    for punct in punctuation:
        normedText = normedText.replace(punct, "")
    return filter(lambda x: x != "", normedText.split(" "))

# <codecell>

words = getMobyDickWords()
print words

# <markdowncell>

# Let's make a dictionary of word frequencies, like from lecture

# <codecell>

frequencies = {}
# Your code here. How do we loop through the words in the 'words' list?

print frequencies

# <markdowncell>

# Now let's get the frequency of the first letters. First, how do we drill down to get at words and their frequencies in the dict we just made?

# <codecell>


# <codecell>

frequenciesLetters = {}

# Your code here. Get the words from our other dictionary and make a new one for the first letters from it.

print frequenciesLetters

# <markdowncell>

# We can sort frequenciesLetters by the keys (i.e., the letters) pretty easily.

# <codecell>


# <codecell>


# <markdowncell>

# But how can we sort by frequency?

# <codecell>


# <codecell>


# <markdowncell>

# # Dictionaries of dictionaries (yo dawg)
# 
# The dictionary below holds verbs. Each verb is the key for a dictionary of its thematic roles. Each thematic role is a dictionary of the sentence structures that the role can appear in with the verb in question.

# <codecell>

thetaMap = {}
thetaMap["destroy"] = {}
thetaMap["destroy"]["Agent"] = [("S", "NP V NP"), ("S", "NP V NP PP.INSTRUMENT")]
thetaMap["destroy"]["Patient"] = [("S", "NP V NP"), ("S", "NP V NP PP.INSTRUMENT"), ("S", "PP.INSTRUMENT V NP")]

# <markdowncell>

# These are very powerful. What does the code below do?

# <codecell>

def struxOverlap(verb, role1, role2):
    global thetaMap
    overlap = []
    verbEntry = thetaMap[verb]
    overlap = [strux for strux in verbEntry[role1] if strux in verbEntry[role2]]
    return overlap

print struxOverlap("destroy", "Agent", "Patient")

# <codecell>


