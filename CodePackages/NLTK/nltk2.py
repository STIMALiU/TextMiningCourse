# NLTK Chapter 2

#To get floating-point division by default (without it, ⅓ is zero!)
from __future__ import division   

# Reading all the books in NLTKs collection to memory (there are nine plus some sentences).
from nltk.book import *

import nltk

nltk.corpus.gutenberg.fileids()

emma = nltk.corpus.gutenberg.words('austen-emma.txt') 
# Note: emma is a 'view' of a corpus file, which acts like a sequence of tokens:
# it can be accessed by index, iterated over, etc.  However, the tokens are only 
# constructed as-needed -- the entire corpus is never stored in memory at once.

emma = nltk.Text(emma) # makes emma a nltk Text object where we can apply nltk's
    # text methods, like concordance.
    
emma.concordance('love')

from nltk.corpus import gutenberg

for fileid in gutenberg.fileids():
    nChars = len(gutenberg.raw(fileid))
    nWords = len(gutenberg.words(fileid))
    nSents = len(gutenberg.sents(fileid))
    nVocab = len(set([w.lower() for w in gutenberg.words(fileid)]))
    print int(nChars/nWords), int(nWords/nSents), int(nWords/nVocab), fileid
    
macbethRaw = gutenberg.raw('shakespeare-macbeth.txt')
macbethWords = gutenberg.words('shakespeare-macbeth.txt')
macbethSents = gutenberg.sents('shakespeare-macbeth.txt')

longestLen = max([len(s) for s in macbethSents])
longestSents = [s for s in macbethSents if len(s) == longestLen]


from nltk.corpus import webtext
webtext.fileids()
for fileid in webtext.fileids():
    print fileid, webtext.raw(fileid)[:65], '...'
    
webtext.raw('pirates.txt').lower().count('jack')   
pirates = nltk.Text(webtext.words('pirates.txt'))


from nltk.corpus import brown
brown.categories()
brown.words(categories = 'news')
brown.words(fileids = ['cg22'])
brown.words(fileids = ['cg22','ca16']) # Concatenates the two corpora into one.

from nltk.corpus import brown
newsText = brown.words(categories = 'news')
fdist = nltk.FreqDist([w.lower() for w in newsText])
modals = ['can','could','may','might','must','will']
for m in modals:
    print m + ':', fdist[m], 

from nltk.corpus import brown
reviewsText = brown.words(categories = 'reviews')
fdist = nltk.FreqDist([w.lower() for w in reviewsText])
modals = ['what','when','where','who','why','good','buy','quality']
for m in modals:
    print m + ':', fdist[m], 

cfd = nltk.ConditionalFreqDist(
    (genre, word)
    for genre in brown.categories() 
    for word in brown.words(categories = genre))
genres = ['news','religion','hobbies','science_fiction','romance','humor']    
modals = ['can','could','may','might','must','will']
cfd.tabulate(conditions = genres, samples = modals)

from nltk.corpus import reuters
reuters.fileids()
reuters.categories(['training/9865', 'training/8666'])
reuters.fileids(['barley','corn'])
reuters.words('training/9865')[:14]
reuters.words(categories = ['corn','barley'])

from nltk.corpus import inaugural
inaugural.fileids()
inaugYears = [fileid[:4] for fileid in inaugural.fileids()]

cfd = nltk.ConditionalFreqDist(
    (target, fileid[:4])
    for fileid in inaugural.fileids()
    for w in inaugural.words(fileid)
    for target in ['america','citizen']
    if w.lower().startswith(target))
cfd.plot()

from nltk.corpus import udhr
languages = ['English','Finnish_Suomi','Italian_Italiano', 'Greenlandic_Inuktikut']
cfd = nltk.ConditionalFreqDist(
    (lang, len(word))
    for lang in languages
    for word in udhr.words(lang + '-Latin1'))
cfd.plot(cumulative = False, title = 'Declaration of Human Rights')

from nltk.corpus import PlaintextCorpusReader
corpusRoot = '/home/mv/Dropbox/Computer/UbuntuInstall'
wordlists = PlaintextCorpusReader(corpusRoot,'.*')
wordlists.fileids()
wordlists.words('things2DoWhenMigrating')[80:100]

def generate_model(cfdist, word, num = 15):
    for i in range(15):
        print word,
        word = cfdist[word].max()
from nltk.corpus import inaugural
obama2009 = inaugural.words('2009-Obama.txt')
bigramsObama2009 = nltk.bigrams(obama2009)
cfdObama2009 = nltk.ConditionalFreqDist(bigramsObama2009)
cfdObama2009['they'].tabulate()
cfdObama2009['they'].plot()
print cfdObama2009['they']
generate_model(cfdObama2009,'they',10)