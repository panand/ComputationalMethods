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
for word in words:
    if word in frequencies:
        frequencies[word] += 1
    else:
        frequencies[word] = 1

print frequencies

# <markdowncell>

# Now let's get the frequency of the first letters. First, how do we drill down to get at words and their frequencies in the dict we just made?

# <codecell>

print frequencies["about"]
print "about"[0]

# <codecell>

frequenciesLetters = {}

# Your code here. Get the words from our other dictionary and make a new one for the first letters from it.
for word in frequencies:
    val = frequencies[word]    
    let = word[0]
    if let in frequenciesLetters:
        frequenciesLetters[let] += val
    else:
        frequenciesLetters[let] = val

print frequenciesLetters

# <markdowncell>

# We can sort frequenciesLetters by the keys (i.e., the letters) pretty easily.

# <codecell>

items = frequenciesLetters.items()
print items

# <codecell>

items.sort(reverse=True)
print items

# <markdowncell>

# But how can we sort by frequency?

# <codecell>

print items[0]
print items[0][1]

# <codecell>

def getCounts(item):
    return item[1]
items.sort(key= getCounts, reverse= True)
print items

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
    overlap = []
    verbEntry = thetaMap[verb]

    overlap = []
    for strux1 in verbEntry[role1]:
        for strux2 in verbEntry[role2]:
            if strux1 == strux2:
                overlap.append(strux1)
    return overlap

    # Faster but less readable alternative using list comprehension
    #overlap2 = [strux for strux in verbEntry[role1] if strux in verbEntry[role2]]
    #return overlap2

if __name__ == "__main__":
    print struxOverlap("destroy", "Agent", "Patient")

# <markdowncell>

# ## Building classes
# 
# Recalling the basics from yesterday: Let's make a simple class and give it an attribute.

# <codecell>

class MyClass(object):
    foo = 5

felix = MyClass()
felix.foo

# <markdowncell>

# Let's give it a method or two.

# <codecell>

class MyClass(object):
    foo = 5
    
    def hello(self): #leave self out and see what happens
        return "Hello world!"
    
    def timesTwo(self, x):
        return x * 2
        
felix = MyClass()
print felix.foo
print felix.hello()
print felix.timesTwo(21)

# <markdowncell>

# Ok, let's make better use of this. I want to make a Coin class with a weight (prob of heads) and a method to flip it that returns 'H' for 'T'

# <codecell>

import random # This lets us generate a random number from 0 to 1, using random.random()

class Coin(object):
    # Create a coin using Coin(nickname, weight)
    def __init__(self, nickname, weight):
        self.nickname = str(nickname)
        self.weight = float(weight)
    
    # Print the coin's name followed by its weight
    def __str__(self):
        return self.nickname + ": " + str(self.weight)
    
    # More complicated __str__ method
    #def __str__(self):
    #    percentH = int(self.weight * 100)
    #    percentT = int(100 - percentH)
    #    return "This coin's called '%s'! \nIt returns heads about %d percent of the time and tails %d percent of the time." % (self.nickname, percentH, percentT)

    # Flip the coin and return 'H' or 'T'
    def flip(self):
        randomPoint = random.random() # Sets randomPoint to a number between 0 and 1
        if randomPoint < self.weight: # Compares the random point with the coin's weight
            return 'H'
        else:
            return 'T'

if __name__ == "__main__":
    lucky = Coin("Lucky",.72)
    print lucky
    print lucky.weight
    print lucky.flip()

# <codecell>

lucky = Coin("Lucky",.72)
fairlady = Coin("The Fair Lady",.5)
bob = Coin("Bob",.2)

coinList = [lucky, fairlady, bob]

for coin in coinList:
    print coin

# <codecell>

for coin in coinList:
    print coin
    flips = []
    for i in range(0,10):
        flips.append(coin.flip())
    print " ".join(flips)

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
# - There should be a method that interacts with the extra atrribute you made.

# <codecell>

class Noun(object):
    
    # Nouns have regular plurals and are count by default.
    # Mass nouns also get regular plurals, in case we ever want to talk about kinds
    def __init__(self,sing,pl=None,mass=False):
        self.sing = str(sing)
        self.mass = mass
        if pl != None:
            self.pl = str(pl)
        else:
            self.pl = self.sing + "s"
            
    def __str__(self):
        return "singular: " + self.sing + "\nplural: " + self.pl + "\nmass noun: " + str(self.mass)
    
    def isCount(self):
        return not self.mass
    
    def thereAre(self, num):
        # Weed out the mass nouns
        if self.mass:
            return "'" + self.sing + "' is a mass noun."
        # Use the singular form if there's only one
        elif num == 1:
            return str(num) + " " + self.sing
        # Use the plural form otherwise, which includes for zero and negative ints
        else:
            return str(num) + " " + self.pl
    
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


