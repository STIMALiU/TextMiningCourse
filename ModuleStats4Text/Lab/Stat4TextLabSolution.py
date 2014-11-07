# Solutions to lab 1

#### MOVIE REVIEWS ####
import nltk
from nltk.corpus import movie_reviews

documents = [(list(movie_reviews.words(fileid)), category)
    for category in movie_reviews.categories()
    for fileid in movie_reviews.fileids(category)]
    
all_words = nltk.FreqDist(w.lower() for w in movie_reviews.words())

word_features = all_words.keys()[:2000]

def document_features(document):
    document_words = set(document)
    features = {}
    for word in word_features:
        features['contains(%s)' %word] = (word in document_words)
    return features
    

featuresets = [(document_features(d),c) for (d,c) in documents]

train_set, test_set = featuresets[100:], featuresets[:100]

movieReviewClassifier = nltk.NaiveBayesClassifier.train(train_set)

print nltk.classify.accuracy(movieReviewClassifier, test_set)

classifyTestData = [movieReviewClassifier.classify(testPoint[0]) for testPoint in test_set]

probPosTestData = [movieReviewClassifier.prob_classify(testPoint[0]).prob('pos') for testPoint in test_set]

movieReviewClassifier.show_most_informative_features(10)



