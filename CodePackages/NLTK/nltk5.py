import nltk
from nltk.book import *
text7.generate() # Generates text using trigrams

# POS
myText = 'This is my text, and I will now try to tag it'
myText = nltk.word_tokenize(myText)
nltk.pos_tag(myText)

nltk.parse.viterbi(myText)

nltk.corpus.brown.tagged_words()[1:10]
