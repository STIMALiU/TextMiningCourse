
myList = ['spam','spam','bacon',2]

myList.append('egg')

myOtherList = ['monty','Python']

myList + myOtherList

myList[1] = myOtherList


# Strings
s = "Mattias"

sentence = 'Guido is the benevolent dictator for life'

sentence.split()


x = array([1,7,3])

X = array([[2,3],[4,5]])


from scipy.linalg import det, inv, eig

a = 2
if a == 1:
	print('a is one')
elif a == 2:
	print('a is two')
else:
	print('a is not one or two')
 
a = 10
while a > 1:
    print("bigger than 1")
    a = a - 1
else:
    print("smaller than 1")
    

word = 'mattias'
for letter in word:
    print(letter)
    
    
myList = ['']*10 
for i in range(10):
    myList[i] = 'mattias' + str(i)
    

myList = [x for x in range(10)]

from math import sin
myList = [sin(x) for x in range(10)] #(don't forget from math import sin)   
 
from scipy import linspace 
myList = [x + y for x in linspace(0.1,1,10) for y in linspace(10,100,10)] #(don't forget from scipy import linspace) 

def mySquare(x):
    return x**2