# Code for the introduction in the text mining course


# NLTK Chapter 1

# Download all the books used in the NLTK book. Only need to do the following command once:
import nltk
# nltk.download()

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

# How long is the book (words and other characters (tokens) like punctuation)?
len(text1)

# How long is the second word?
len(text1[1])

# Give me the set of distinct tokens!
set(text1)

# How many tokes among the first 100 words?
len(set(text1[0:99]))

# Python is nice because return arguments can be directly subsetted:
sorted(set(text1))[900:910]

# Lexical richness (#words/#distinct tokens) [Don’t forget from __future__ import division, otherwise 1/2=0 !]
from __future__ import division
len(text1)/len(set(text1))

# How many times does a word appear in the text?
text1.count("do")

# Percentage of the text occupied by a word, see E28 below for a better function.
from nltk.book import text5 # Chat conversations
100*text5.count("call")/len(text5)
100*text5.count("whatever")/len(text5)

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

# List comprehension
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



#### MOVIE REVIEWS ####
import nltk
from nltk.corpus import movie_reviews

movie_reviews.categories()
movie_reviews.fileids('pos')
movie_reviews.fileids('neg')
movie_reviews.words('neg/cv729_10475.txt')
len(movie_reviews.words('neg/cv729_10475.txt'))

documents = [(list(movie_reviews.words(fileid)), category)
    for category in movie_reviews.categories()
    for fileid in movie_reviews.fileids(category)]
    
documents[0][0][0:100] # Show the 100 first words in the first review

documents[0][1]  # Shows whether the first review was labelled as positive or negative

all_words = nltk.FreqDist(w.lower() for w in movie_reviews.words())

word_features = all_words.keys()[:1000]

# Function that turns a document into a explanatory variables (features)
def document_features(document,word_features):
    document_words = set(document)
    features = {}
    for word in word_features:
        features['contains(%s)' %word] = (word in document_words)
    return features
    
featuresDoc = document_features(movie_reviews.words('pos/cv957_8737.txt'),word_features)

featuresDoc['contains(recommend)'] 

featuresets = [(document_features(d,word_features),c) for (d,c) in documents]

featuresets[95][0]['contains(excellent)'] # Does review no. 95 contain the word 'excellent'?
featuresets[95][1]                        # What was the verdict?
 
train_set, test_set = featuresets[100:], featuresets[:100]

movieReviewClassifier = nltk.NaiveBayesClassifier.train(train_set)

print nltk.classify.accuracy(movieReviewClassifier, test_set)

movieReviewClassifier.show_most_informative_features(10)