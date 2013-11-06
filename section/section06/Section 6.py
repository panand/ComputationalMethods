# -*- coding: utf-8 -*-
# <nbformat>3.0</nbformat>

# <markdowncell>

# # Welcome to week 6!
# 
# This notebook is in my repository at http://github.com/obnorthrup/144coursework
# 
# ## Today: Regular Expressions and tree structures in Python
# 
# We've seen that regex alone can't match parentheses. Let's augment it with Python to solve that problem (in a couple steps). Later, we'll convert a properly matched string into a tree representation.
# 
# #### Version 1: Counting parens
# 
# Use any method from the `re` module to search the input string. Return True if there are an equal number of open and close parens, and False otherwise.

# <codecell>

import re

def isMatched(string):
    matches = re.findall(r'[\(\)]',string)
    pairCount = 0
    for m in matches:
        if m == '(':
            pairCount += 1
        else:
            pairCount += -1
    if pairCount == 0:
            return True
    return False

if __name__ == "__main__":
    goodTest = "(the (quick (brown (fox))))"
    badTest = "(the (quick brown (fox))))"
    print isMatched(goodTest)
    print isMatched(badTest)

# <markdowncell>

# All it takes is regular expressions plus a counter.

# <markdowncell>

# #### Version 2:
# 
# This code works for the `goodTest` and `badTest` inputs above, but fails on `weirdTest`. That's because if all we do is count blindly, `"()"` and `")("` are equally well-formed. Rewrite your function to return False for illformed inputs like `weirdTest`.

# <codecell>

import re

def isMatched(string):
    matches = re.findall(r'[\(\)]',string)
    pairCount = 0
    for m in matches:
        if m == '(':
            pairCount += 1
        else:
            pairCount += -1
            if pairCount < 0: # if pairCount ever goes negative, it means we've seen an unmatched closed paren
                return False
    if pairCount == 0:
            return True
    return False

if __name__ == "__main__":
    goodTest = "(the (quick (brown (fox))))"
    badTest = "(the (quick brown (fox))))"
    weirdTest = ")()("
    print isMatched(goodTest)
    print isMatched(badTest)
    print isMatched(weirdTest)

# <markdowncell>

# ## Challenge
# 
# Instead of a boolean value, return a constituent structure of lists. So the input `((Brigid) (followed (the detective)))` should yield `[["Brigid"], ["followed", ["the", "detective"]]]`.
# 
# **Note**: This is hard. The actual code is less important than thinking about how you'd do it. There are better solutions than this, and we'll talk more about parsing trees next week.

# <codecell>

import re

def listParse(string):
    
    # To start, check if the string is a licit input, and return an error message if not
    if not isMatched(string):
        return "This input is not grammatical."
    
    # First approach uses string.split, but it's long.
    #nonwordsRE = re.compile(r'(\W)')
    #rawList = nonwordsRE.split(string)
    #filteredList = []
    #for item in rawList:
    #    if item == '' or item == ' ':
    #        pass
    #    else:
    #        filteredList.append(item)
    
    # Make a list of words and open and close parens
    rawList = re.findall(r'\w+|\(|\)', string)
    
    # We'll replace parts of the list iteratively the list of strings becomes a tree structure
    # Preserve rawList, just in case
    curtree = rawList
    
    # Danger! An infinite loop will be created if the code inside the while loop does not eventually get rid of all '(' items
    while '(' in curtree:
        
        # Keep track of the index of the most recent open paren
        lastOpen = None
        
        # Walk through curtree, remembering open parens and looking for a closing one
        for i in range(len(curtree)):
            v = curtree[i]
            if v == '(':
                # Save the index of the most recent open parens, to mark the start of the subtree
                lastOpen = i
            if v == ')':
                # Get everything within the pair of parenthesis as a new list
                subtree = curtree[lastOpen+1:i]
            
                # Make a new version of the tree, with the new list replacing whatever was in its place
                newtree = curtree[:lastOpen]
                newtree.append(subtree)
                newtree += curtree[i+1:]
            
                # Some code so we can see what's happened on each loop
                print '''Found a close paren at index {i} with input {curtree}
                - Last open parens found at index {lastOpen}
                - Subtree built this pass: {subtree}
                - Input for next pass: {newtree}
                '''.format(i=i, lastOpen=lastOpen, subtree=subtree, curtree=curtree, newtree=newtree)
                
                # Set curtree to newtree and break so we can loop through again
                curtree = newtree
                break
            
    return curtree

if __name__ == "__main__":
    maltese = "((Brigid) (followed (the detective)))"
    print listParse(maltese)

# <codecell>

quick = "((The (quick brown fox)) (jumped (over (the (lazy dog)))))"
print listParse(quick)

# <codecell>


