import nltk

from nltk.book import *

punctuation = ['.',':',',','?','!','-','--',';']    
text2Clean = [w for w in text2 if w not in punctuation]

text2Clean[1:10]

nltk.bigrams(text2Clean[1:10])

nltk.trigrams(text2Clean[1:10])

unigramModel = nltk.NgramModel(1, text2Clean)

len(set(text2Clean))

unigramModel.generate(num_words = 50)

bigramModel = nltk.NgramModel(2, text2Clean)

bigramModel.generate(num_words = 50)

trigramModel = nltk.NgramModel(3, text2Clean)

trigramModel.generate(num_words = 50)


# POS
nltk.corpus.brown.tagged_words()[1:10]

myText = 'This is my text, and I will now try to tag it'

myText = nltk.word_tokenize(myText)

nltk.pos_tag(myText)

nltk.parse.viterbi(myText)


