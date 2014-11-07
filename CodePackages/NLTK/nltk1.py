# NLTK Chapter 1

# Download all the books used in the NLTK book. Only need to do the following command once:
import nltk
# nltk.download()

#To get floating-point division by default (without it, ⅓ is zero!)
from __future__ import division

# Reading all the books in NLTKs collection to memory (there are nine plus some sentences).
from nltk.book import *

# If you only want one of them, say text1, do the obvious:
from nltk.book import text1

# text1, text2,...,text9 are nine different text object. More specifically, each object is of class nltk.text.Text
text1[1]    # returns the second (note that python indexes start with 0) word of the first book in the collection, Moby Dick. 
                # text1[1] is a string object
text1[1][2] # is the third letter of the second word in Moby Dick.

# You can of course define your own text (as a Python list object):
myText = ["This", "is", "my","text","and","there","is","nothing","you","can","do","about","it","!"]
myText[4]


## Searching Text ##
text1.concordance("monstrous")  # Searches for occurences of words and displays part of the lines where it appear 
                                # (i.e. it also gives the context in which the word appears)

#text1.similar("whatever") # Lists the words that are similar to some word (similar in which sense?)

#text2.common_contexts(["monstrous","very"])

# Dispersion plot - To find out WHERE a word appears (you need the module pylab which ships with the Spyder IDE)
text4.dispersion_plot(["citizens", "democracy", "freedom", "duties", "America"]) 

# How long is the book (words and other characters (tokens) like punctuation)?
len(text1)

# How long is the second word?
len(text1[1])

# Give me the set of distinct tokens!
set(text1)

# How many tokes among the first 100 words?
len(set(text1[0:99]))


mobyTokens = set(text1)
type(mobyTokens)    # set() returns a SET object, which cannot be indexed. 
                        # This gives an error mobyTokens[1]

# But set objects can be sorted:
sorted(mobyTokens)

# Actually, any Python list object can be sorted:
sorted(myText)

# Python is nice because return arguments can be directly subsetted:
sorted(mobyTokens)[900:910]

# Lexical richness (#words/#tokens) [Don’t forget from __future__ import division]
len(text1)/len(set(text1))

# How many times does a word appear in the text?
text1.count("do")

# Percentage of the text occupied by a word, see E28 below for a better function.
from nltk.book import text5 # Chat conversations
100*text5.count("mildly")/len(text5)

# Define a function that computes lexical diversity
def lexical_diversity(text):
        return len(text)/len(set(text))

#Note that our new function can be used on any text, even your own:
lexical_diversity(myText)

# You can combine two lists with text (the addition operator concatenates strings and lists):
myText1 = ["This", "is", "my","text","and"]

myText2 = ["there","is","nothing","you","can","do","about","it","!"]

myText1 + myText2

# Adding a word to a list (appending a word)
myText.append("LOL")

# We can find the FIRST position of given word:
myText.index('about')

# Frequency distribution
from nltk import FreqDist

fdist1 = FreqDist(text1)

vocabulary = fdist1.keys()

frequencies = fdist1.values()

fdist1['whale']

fdist1.plot(20)

fdist1.plot(20, cumulative = True)   

# Finding the really long words (using Pythons list comprehension):
V = set(text1)

[w for w in V if len(w)>15]

# Note that the variable w in the list comprehension is just a dummy. The following gives the same result
[whatever for whatever in V if len(whatever)>15]

# Finding the long words (more than seven letters) that appear more than seven times
[w for w in V if len(w)>7 and fdist1[w]>7]

# Counting the number of characters in each word in a text
[len(w) for w in text1]

# Bigram function returns a list of bigrams
from nltk import bigrams, trigrams

bigrams(myText2)

trigrams(myText2)

bigramsText1 = bigrams(text1) # bigramsText1[0] is the tuple containing the first bigram

# Collocations are frequent bigrams from words that are not so common as unigrams. 
# This function returns nothing, just prints the collocations to screen
text1.collocations()

# Computing the frequency distribution of word lengths. Returns a dictionary.
fdistWordLength = FreqDist([len(w) for w in text1])

fdistWordLength.keys() # The different word lengths
fdistWordLength.values() # The frequency of each word length
fdistWordLength.items() # Shows both keys and values at the same time

fdist1['the']
fdist1.freq('the') # Frequency of the word ‘the’
fdist1.max()

# String methods

s = "MatTias"

s.lower()

s.upper()

s.startswith("ma")

"T" in s

# Find all the words in Moby Dick that ends with -ableness. Sort then alphabetically.
from nltk.book import text2, text3, text5, text7
sorted([w for w in set(text1) if w.endswith('ableness')])

sorted([w for w in set(text7) if '-' in w and 'index' in w])

sorted([wd for wd in set(text3) if wd.istitle() and len(wd) > 10])

sorted([w for w in set(text7) if not w.islower()])

sorted([t for t in set(text2) if 'cie' in t or 'cei' in t])

import nltk
nltk.chat.chatbots()






































# EXERCISES Chapter 1

# E1
# E2
# E3
3*sent1
# E4
len(text2)
len([w.lower() for w in set(text2) if w.isalpha()])
# E5
# E6
text2.dispersion_plot(["Elinor","Marianne","Edward","Willoughby"])
# E7
text5.collocations()
# E8
# E9 a))
myString = "I can write whatever I feel like here"
print myString
# E9 b)
otherString = ", I can"
myString + otherString
myString + " " + otherString
" ".join([myString,otherString]) # Pythonista Alternative

# E10
mySent = ["This","is","my","sentence"]
sentence = " ".join(mySent)
sentence.split()
# E11
phrase1 = ["This","is","my","sentence"]
phrase2 = ["And","there","is","nothing","you","can","so","about","it"]
" ".join(phrase1 + phrase2)
len(phrase1 + phrase2) - (len(phrase1) + len(phrase2))
# E12
# E13
sent1[2][2]
# E14
[sent3[i] == "the" for i in range(len(sent3))]
[sent3[i] == "the" for i,w in enumerate(sent3)] # Alternative
# E15
sorted([w for w in text5 if w.startswith("b")])
# E16
# E17
text9.index('sunset')
text9[621:644]
# E18
sorted(set(sent1 + sent2 + sent3 + sent4 + sent5 + sent6 + sent7 + sent8 + sent9))
# E19
# E20
# not w.islower() is True for punctuation, whereas w.isupper() is False
# E21
text2[-2:]
# E22
fourLetterWords = [w for w in text5 if len(w) == 4]
FreqDist(fourLetterWords).items()
FreqDist(fourLetterWords).plot()
#E23
for i in range(len(text6)):
        if text6[i].isupper():
                print text6[i]
#E24
[w for w in set(text6) if w.endswith("ize") and w.isalpha()]        
[w for w in set(text6) if "z" in w  and w.isalpha()]
[w for w in set(text6) if "pt" in w  and w.isalpha()]
[w for w in set(text6) if w.isalpha() and w[1:].islower() and w[0].isupper()]
#E25a
sent = ["she","sells","sea","shells","by","the","sea","shore"]
for w in sent:
        if w.startswith("sh"):
                print w
# E25b
for w in sent:
        if len(w)>4:
                print w        

# E26
averageWordLength = sum([len(w) for w in text1])/len(text1)        

# E27. Not sure about this one since not all elements from set are words.
def vocabSize(text):
        ''' Computes vocabulary size of text. Words are defined liberally, including 
        punctuation and other non-letter symbols '''
        return len(set(text))
vocabSize(text1)

# E28
def percent(word, text):
        ''' Computes the percentage that word appears in text '''
        count = text.count(word.lower()) + text.count(word.upper()) + text.count(word[0].upper() 
                                                                                 + word[1:].lower())
        return 100*count/len(text)
percent('Lol',text5)

# E29
# set1 < set2 is True if every element of set1 is an element of set2
# Can be used to check if a sentence is a part of another sentence. 