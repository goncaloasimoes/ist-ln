from KB import loadXMLandDivideTest, loadXMLandDivideRandomly
from mainbot import processTest
from preprocessing import remove_new_line, remove_leading_trailing_whitespace
import random as rnd 

ret = loadXMLandDivideTest('./data/KB.xml', .20)
KB = ret[0]
test = ret[1]

# TODO: preprocess KB
preprocessing = lambda x: remove_leading_trailing_whitespace(
                            remove_new_line(x)
                        ) # TODO:
k = 0
for question in KB:
    KB[k,0] = preprocessing(question[0])
    k+=1
#print(KB)

# TODO: add functions of preprocessing and similarity
resultsList = processTest(
    KB, 
    test, 
    lambda x: x, # preprocessing
    lambda x,y: rnd.randint(0,100) # similarity
)

# TODO: get measures
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
