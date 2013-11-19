#!/usr/env python

import subprocess
import json
from nltk.tree import ParentedTree

import pdb

class SearchTree(ParentedTree):
    def loadMatches(self, e):
        self.e = e
        self.handles = {}
        self.handlePositions = {}
        self.filename = e["filename"]
        self.treenumber = e["treeNumber"]
        matchNumber = e["matchTreeNumber"] - 1
        self.matchTree = self.getTreeDepthFirstNumber(matchNumber)
        for handle,structure in e["nodes"].items():
            try:
                loc = int(structure["treeNumber"]) -1
                # NOTE: this doesn't deal with leaf handles, because they are strings; probably should stick with the tree positions...
                self.handles[handle] = self.getTreeDepthFirstNumber(loc)
                self.handlePositions[handle] = loc
            except:
                pass
    
    def getTreeDepthFirstNumber(self, num):
        return self[self.treepositions()[num]]
    
    def makeJSON(self, handles, position):
        out = {"name": self.node, "type": "nonterm" , "children": [], "position": position}

        # is this a handle, perhaps?
        for handle,treelet in handles.items():
            if treelet == self:
                out["handle"] = handle
                break
        
        
        for child in self:
            if isinstance(child, basestring): # is this a leaf?
                chOut,position = self.makeJSONleaf(child, handles, position+1)
            else:
                chOut,position = child.makeJSON(handles, position+1)
            out["children"].append(chOut)

        return (out, position)
    
    def makeJSONleaf(self, element, handles, position):
        out = {"name": element, "type": "term", "position": position}
    
        for handle,treelet in handles.items():
            if treelet == self:
                out["handle"] = handle
                break
        
        return (out, position)
        
class Treebank():

    javaJars = "/Users/panand/144/class/scripts/*:/Users/panand/144/class/scripts/stanford-tregex-2013-06-20/stanford-tregex.jar"
    javaPath = "/usr/bin/java"
    programLoc = "edu.ucsc.TregexWrapper.TregexWrapper"
    
    trees = []
    def __init__(self, dir, pattern, javaJars=None, javaPath=None):
        self.dir = dir
        self.pattern = pattern
        if javaJars:
            self.javaJars = javaJars

        if javaPath:
            self.javaPath = javaPath
        
    def run(self):
        print "Running tregex..."
        raw = subprocess.check_output(["java", "-cp", self.javaJars, self.programLoc, self.pattern, self.dir], stderr=subprocess.STDOUT)
        print "Processing output..."
        for ma in raw.split("\n"):
            try:
                m = json.loads(ma)
                tree = SearchTree(m["tree"])
            except:
                pass
            else:
                tree.loadMatches(m)
                self.trees.append(tree)
        print "Done!"

    def __getitem__(self, key):
        return self.trees[key]

    def __len__(self):
        return len(self.trees)

if __name__ == "__main__":
    dir = "/Users/panand/144/class/data/Corpora/treebank_3/parsed/mrg/wsj/24/"
    pattern = "(NP . NP)"
    
    t = Treebank(dir, pattern)
    t.run()
    print t[0:3]
