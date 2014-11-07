# NLTK Chapter 6

import nltk 

##### NAME CLASSIFICATION ######
# This is the feature constructor that we will use for classifying names
def gender_features(word):
    return {'last_letter' : word[-1], 'first_letter' : word[0], 'name_length' : len(word)}
    
gender_features('Mattias')

from nltk.corpus import names
import random
# Reading in a lot of names from files male.txt and female.txt and organizing
# them as tuples of the form (name, sex)
names = ([(name,'male') for name in names.words('male.txt')] + 
    [(name,'female') for name in names.words('female.txt')])
random.shuffle(names)    
names[150:160]

# Setting up the feature matrix (like term-document matrix in R) and the response variable (true sex)
featuresets = [(gender_features(n),g) for (n,g) in names]

# Splitting the data into training and testing sets
train_set, test_set = featuresets[500:], featuresets[:500]

# Train the classifier
nameClassifier = nltk.NaiveBayesClassifier.train(train_set)

# Test some predictions for my family members (all correct!)
nameClassifier.classify(gender_features('mattias'))
nameClassifier.classify(gender_features('camilla'))
nameClassifier.classify(gender_features('adam'))
nameClassifier.classify(gender_features('elma'))

# Compute the classifier's accuracy on the test set
print nltk.classify.accuracy(nameClassifier, test_set)

# Print the 30 most informative features:
nameClassifier.show_most_informative_features(30)


#### MOVIE REVIEWS ####
import nltk
from nltk.corpus import movie_reviews

documents = [(list(movie_reviews.words(fileid)), category)
    for category in movie_reviews.categories()
    for fileid in movie_reviews.fileids(category)]
    
documents[0][0][0:100] # Show the 100 first words in the first review

documents[0][1]  # Shows whether the first review was labelled as positive or negative

all_words = nltk.FreqDist(w.lower() for w in movie_reviews.words())

word_features = all_words.keys()[:2000]

def document_features(document):
    document_words = set(document)
    features = {}
    for word in word_features:
        features['contains(%s)' %word] = (word in document_words)
    return features
    
featuresDoc = document_features(movie_reviews.words('pos/cv957_8737.txt'))

featuresDoc['contains(recommend)'] 

featuresets = [(document_features(d),c) for (d,c) in documents]

train_set, test_set = featuresets[100:], featuresets[:100]

movieReviewClassifier = nltk.NaiveBayesClassifier.train(train_set)

print nltk.classify.accuracy(movieReviewClassifier, test_set)

movieReviewClassifier.show_most_informative_features(10)

