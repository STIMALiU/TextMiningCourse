#install.packages("tm") # Text mining
library(tm)

reviewsNeg <- Corpus(DirSource("/home/mv/nltk_data/corpora/movie_reviews/neg", encoding = "UTF-8"))
reviewsPos <- Corpus(DirSource("/home/mv/nltk_data/corpora/movie_reviews/pos", encoding = "UTF-8"))
inspect(reviewsNeg[1:2])
reviewsNeg[[10]]
reviews <- c(reviewsNeg,reviewsPos)

#reviews <- tm_map(reviews, stripWhitespace)
#reviews <- tm_map(reviews, tolower)
#reviews <- tm_map(reviews, removeWords, stopwords("english"))
#reviews <- tm_map(reviews, stemDocument)

dtmReviews <- DocumentTermMatrix(reviews, control = list(removePunctuation = TRUE, 
                                                         stopwords = TRUE, 
                                                         minDocFreq=5, 
                                                         removeNumbers=TRUE ))

inspect(dtmReviews[1:10,10:100])

freqWords <- findFreqTerms(dtmReviews, 1000)

#dtmReviewsSparse <- removeSparseTerms(dtmReviews, 0.4)

dtmReduced <- DocumentTermMatrix(reviews, list(dictionary = freqWords))

dtmDataFrame <- as.data.frame(inspect(dtmReduced))

y = c(rep('Neg',1000),rep('Pos',1000)) # Creates the response vector (i.e. the labels)

# Shuffling the data randomly, creating training and test datasets
randomIdx <- sample(2000)
y <- y[randomIdx]
X <- dtmDataFrame[randomIdx,]

# Training on 1500 observations - testing on 500 observations
yTrain <- as.factor(y[1:1500])
XTrain <- X[1:1500,]
yTest <- as.factor(y[1501:2000])
XTest <- X[1501:2000,]

# Remove terms that were never seen in training data
appearAtLeastOnce <- colSums(XTrain)>0
XTrain <- XTrain[,appearAtLeastOnce]
XTest <- XTest[,appearAtLeastOnce]

# Training an off-the-shelf SVM
install.packages("e1071")
library(e1071) # Contains the svm() function
svmModel <- svm(XTrain,yTrain)
print(svmModel)

pred <- predict(svmModel,XTest)
confusionMatrix <- table(pred, yTest)
Precision = confusionMatrix[1,1]/sum(confusionMatrix[1,])
Recall = confusionMatrix[1,1]/sum(confusionMatrix[,1])

