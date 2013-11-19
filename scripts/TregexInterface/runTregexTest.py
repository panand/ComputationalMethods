import runTregex

rawInput = """{"tree":"( (S (S (PP (IN In) (NP (JJ American) (NN romance))) (, ,) (NP-SBJ-2 (RB almost) (NN nothing)) (VP (VBZ rates) (S (NP-SBJ (-NONE- *-2)) (ADJP-PRD (ADJP (JJR higher)) (PP (IN than) (SBAR-NOM (WHNP-1 (WP what)) (S (NP-SBJ (DT the) (NN movie) (NNS men)) (VP (VB have) (VP (VBN called) (S (NP-SBJ (-NONE- *T*-1)) (`` ``) (S-NOM-PRD (NP-SBJ (-NONE- *)) (VP (NN meeting) (NP (JJ cute)))) ('' ''))))))))))) (: --) (S (S-ADV (NP-SBJ (DT that)) (VP (VBZ is))) (, ,) (NP-SBJ (NN boy-meets-girl)) (VP (VBZ seems) (ADJP-PRD (RB more) (JJ adorable)) (SBAR-ADV (IN if) (S (NP-SBJ (PRP it)) (VP (VBZ does) (RB n't) (VP (VB take) (NP (NN place)) (PP (IN in) (NP (NP (DT an) (NN atmosphere)) (PP (IN of) (NP (ADJP (JJ correct) (CC and) (JJ acute)) (NN boredom))))))))))) (. .)))","nodes":{},"matchTreeNumber":119,"filename":"parsed\/mrg\/brown\/cf\/cf01.mrg","matchTree":"(PP (IN of) (NP (ADJP (JJ correct) (CC and) (JJ acute)) (NN boredom)))","treeNumber":1}"""

import json

raw = json.loads(rawInput)

tr = runTregex.SearchTree(raw["tree"])

tr.loadMatches(raw)

tr.makeJSON(tr.handles)