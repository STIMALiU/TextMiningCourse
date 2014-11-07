install.packages('e1071')
library('e1071')

data1 <- seq(1,10,by=2)
classes1 <- c('a','a','a','b','b')
test1 <- seq(1,10,by=2) + 1

model1 <- svm(data1,classes1,type='C',kernel='linear')
print(model1)
summary(model1)

predict(model1,data1)
pred <- fitted(model1)
table(pred, classes1)

predict(model1,test1)


# Task2

data2 <- seq(1,10)
classes2 <- c('b','b','b','a','a','a','a','b','b','b')

model2 <- svm(data2,classes2,type='C',kernel='linear')

predict(model2,data2)
table(predict(model2,data2), classes2)

model3 <- svm(data2,classes2,type='C',kernel='radial')

predict(model3,data2)
table(predict(model3,data2), classes2)



svm1 <- svm(dtmDataFrame,y,type='C',kernel='linear')

glmnetFit <- glmnet(as.matrix(XTrain), yTrain, family="binomial")
predict(glmnetFit, XTest)