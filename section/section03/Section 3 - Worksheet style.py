# -*- coding: utf-8 -*-
# <nbformat>3.0</nbformat>

# <markdowncell>

# # Welcome to week 3!
# 
# #### Plan
# 
# - Dictionaries
# - Classes

# <markdowncell>

# ## Fun with dictionaries
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

#def notEmpty(string):
#    return string != ""

# <codecell>

words = getMobyDickWords()
print words

# <markdowncell>

# Let's make a dictionary of word frequencies, like from lecture last Wednesday

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

# ## Dictionaries of dictionaries (yo dawg)
# 
# The dictionary below holds verbs. Each verb is the key for a dictionary of its thematic roles. Each thematic role is a dictionary of the sentence structures that the role can appear in with the verb in question.

# <codecell>

thetaMap = {}
thetaMap["destroy"] = {}
thetaMap["destroy"]["Agent"] = [("S", "NP V NP"), ("S", "NP V NP PP.INSTRUMENT")]
thetaMap["destroy"]["Patient"] = [("S", "NP V NP"), ("S", "NP V NP PP.INSTRUMENT"), ("S", "PP.INSTRUMENT V NP")]

# <codecell>

thetaMap

# <markdowncell>

# Next, let's use this for something. Let's see what syntactic structures involving the ver 'destroy' have both an Agent and a Patient.

# <codecell>

def struxOverlap(verb, role1, role2):
    """
    Lists possible syntactic structures containing a given verb and two given thematic arguments
    
    Arguments:
        verb (string), a verb key in thetaMap
        role1 (string), a theta role key in thetaMap[verb]
        role2 (string), another theta role key in thetaMap[verb]
    
    Returns:
        overlap (list), the structures shared by thetaMap[verb][role1] and thetaMap[verb][role2]
        
    Raises:
        nothing
    """
    return []

if __name__ == "__main__":
    print struxOverlap("destroy", "Agent", "Patient")

# <markdowncell>

# ## Building classes
# 
# Recalling the basics from yesterday: Let's make a simple class and give it an attribute.

# <codecell>


# <markdowncell>

# Let's give it a method or two.

# <codecell>


# <markdowncell>

# Ok, let's make better use of this. I want to make a Coin class with a weight (prob of heads) and a method to flip it that returns 'H' for 'T'

# <codecell>


# <codecell>


# <codecell>


# <markdowncell>

# Anyway, that's not linguistics. Let's made a more useful class!

# <markdowncell>

# ## Noun class
# 
# Let's build a class called **Noun**. It should do the following:
# 
# - Nouns have singular and plural forms, a mass/count distinction, (and something else of your choice)
# - All of these should work:
#     - `apple = Noun("apple")`  
#       `goose = Noun("goose","geese")`  
#       `gohan = Noun("rice",mass=True)`
#     - I.e., If we don't specify a plural, it should be set automatically, and nouns are count unless specified
# - Printing an instance of Noun should tell you everything you know about it, in a readable way.
# - The method `isCount()` should tell you whether the noun is mass or count.
# - The method `thereAre(int)` should pluralizes correctly, given how many of the noun there are:
#     - `apple.thereAre(3)` returns the string `"3 apples"`
#     - `apple.thereAre(1)` returns the string `"1 apple"`
#     - `gohan.thereAre(4)` returns the string `"'rice' is a mass noun"`
# - There should be a method that interacts with the extra atrribute you made, or changes something about the noun. Maybe a quick way to regularize the plural?

# <codecell>

class Noun(object):
    
    # Your code here. You'll need to add __init__, __str__, isCount, and thereAre, at least.
    
def testCases():
    '''Makes entries for "apple", "goose", and "rice"'''
    apple = Noun("apple")
    print apple
    print apple.isCount()
    print apple.thereAre(4)
    print apple.thereAre(1)
    print apple.thereAre(0)

    print

    goose = Noun("goose","geese")
    print goose
    print goose.isCount()
    print goose.thereAre(4)
    print goose.thereAre(1)
    print goose.thereAre(0)

    print

    gohan = Noun("rice",mass=True)
    print gohan
    print gohan.isCount()
    print gohan.thereAre(4)
    print gohan.thereAre(1)
    print gohan.thereAre(0)
    
if __name__ == "__main__":
    testCases()

# <codecell>


