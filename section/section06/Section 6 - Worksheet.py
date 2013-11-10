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
    
    # Your code here
    
    return False

if __name__ == "__main__":
    goodTest = "(the (quick (brown (fox))))"
    badTest = "(the (quick brown (fox))))"
    print isMatched(goodTest) # Should be True
    print isMatched(badTest) # Should be False

# <markdowncell>

# #### Version 2:
# 
# This code works for the `goodTest` and `badTest` inputs above, but fails on `weirdTest`. That's because if all we do is count blindly, `"()"` and `")("` are equally well-formed. Rewrite your function to return False for illformed inputs like `weirdTest`.

# <codecell>

import re

def isMatched(string):
    
    # Your code here
    
    return False

if __name__ == "__main__":
    goodTest = "(the (quick (brown (fox))))"
    badTest = "(the (quick brown (fox))))"
    weirdTest = ")()("
    print isMatched(goodTest) # Should be True
    print isMatched(badTest) # Should be False
    print isMatched(weirdTest) # Should be False

# <markdowncell>

# ## Challenge
# 
# Instead of a boolean value, return a constituent structure of lists. So the input `((Brigid) (followed (the detective)))` should yield `[["Brigid"], ["followed", ["the", "detective"]]]`.
# 
# **Note**: This is hard. The actual code is less important than thinking about how you'd do it.

# <codecell>

import re

def listParse(string):
    
    # Your code here.
            
    return string # Change this to return return the list where you've built your tree

if __name__ == "__main__":
    maltese = "((Brigid) (followed (the detective)))"
    print listParse(maltese)

# <codecell>

quick = "((The (quick brown fox)) (jumped (over (the (lazy dog)))))"
print listParse(quick)

# <codecell>


