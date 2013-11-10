# Section notes for Week 5

No IPython Notebook today! Instead, load up [Debuggex](https://www.debuggex.com/), switch it to Python mode, and turn on the verbose flag. You can find this document in my repo at [http://github.com/obnorthrup/144coursework](http://github.com/obnorthrup/144coursework).

![RegEx](http://claylevering.com/wp-content/uploads/2012/02/fts-regex-front.jpeg)

**Note:** There's no 'complete' version of this week's notes, so make sure you're saving your responses and writing comments as we go.

### Parsing links in HTML

Here's an edited chunk of text from the Wikipedia entry on [Chomsky (1957)](http://en.wikipedia.org/wiki/Syntactic_Structures). Find all the links to other pages on Wikipedia.

    <p><i>Syntactic Structures</i> also initiated an interdisciplinary dialog between <a href="/wiki/Philosophy_of_language" title="Philosophy of language">philosophers of language</a> and linguists. American philosopher <a href="/wiki/John_Searle" title="John Searle">John Searle</a> wrote that "Chomsky's work is one of the most remarkable intellectual achievements of the present era, comparable in scope and coherence to the work of <a href="/wiki/Keynes" title="Keynes" class="mw-redirect">Keynes</a> or <a href="http://psychclassics.yorku.ca/Freud/Dreams/dreams.pdf" title="Freud" class="mw-redirect">Freud</a>. It has done more than simply produce a revolution in linguistics; it has created a new discipline of generative grammar and is having a revolutionary effect on two other subjects, philosophy and psychology".<sup id="cite_ref-Searle_1972_3-2" class="reference"><a href="#cite_note-Searle_1972-3">3</a></sup> Chomsky and Willard Van Orman Quine, a stridently anti-mentalistic philosopher of language and one of Chomsky's early influences, debated many times on the merit of Chomsky's linguistic theories. Most philosophers supported Chomsky's idea that natural languages are innate and syntactically rule-governed. In addition, they thought that there also exist rules in the human mind which bind meanings to utterances. The investigation of what these rules might be started a new era in <a href="/wiki/Philosophical_semantics" title="Philosophical semantics" class="mw-redirect">philosophical semantics</a>.</p>

Link to this chunk in plain text, if the above is hard to grab: [Click here](https://raw.github.com/obnorthrup/144coursework/master/section/Section%205/chomsky.txt).

### Disjunction

Put the text below into Debuggex and match all occurrences of the word `we` or `We`. Then, stop it from matching `we're`.

♫

    We are young, heartache to heartache we stand 
    No promises, no demands 
    Love Is A Battlefield 
    We are strong, no one can tell us we're wrong 
    Searchin' our hearts for so long, both of us knowing 
    Love Is A Battlefield

♪♫

### #whatshouldwecallregex

Put any of the tweets below into Debuggex and match the hashtags. Include a group that excludes the `#`, and name it 'tag'. _Optional: While you're at it, match links too, as a group called 'url'._

    @natalieohayre I agree #hc09 needs reform- but not by crooked politicians who r clueless about healthcare! #tcot #fishy NO GOV'T TAKEOVER!
    
    Dear OBAMA "Hessian"" Barrak: If you a best presiden. Why I not have twelve bread and more house? #giveMeSandwichOrGiveMeTwoSandwich
    
    The ultimate hedge: "This appears to suggest that..." #academia
    
    Anybody else go all #RitaRepulsa when they have a headache? http://t.co/scUDnJ0LbL #itsmorphintime


### Parsing

Put the text below into Debuggex and match all the acronyms/initialisms.

    That U.S.A. poster-print from NG costs $12.40, and there are 1,259,000 copies with 32% of stores already sold out.  It runs the gamut from A...Z!

_More parsing problems_:

1. Match words, with optional hyphens
2. Match currency or percentages 
3. Match punctuation seperately, but treat the ellipsis (…) as a single match
4. Put all of these together (including the acronym solution) to parse all words in the string as matches.

---

_Note: Some of today's exercises are adapted from [here](http://classes.ischool.syr.edu/ist664/NLPfall2013/)._
