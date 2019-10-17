from KB import loadXMLandDivideTest, loadXMLandDivideRandomly
from mainbot import processTest
import random as rnd 

ret = loadXMLandDivideTest('./data/KB.xml', .20)
KB = ret[0]
test = ret[1]

# TODO:
resultsList = processTest(
    KB, 
    test, 
    lambda x: x, 
    lambda x,y: rnd.randint(0,100)
)

#
correct = 0
wrong = 0
k = 0
for result in resultsList:
    if result == test[k,1]:
        correct += 1
    wrong += 1
    k += 1

print(correct)
print(wrong)
print('Test Accuracy: ' + str(correct/test.shape[0]))