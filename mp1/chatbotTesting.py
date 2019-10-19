from KB import loadXMLandDivideVali, loadXMLandDivideRandomly
from mainbot import processTest
from preprocessing import combination
from similarity import jaccard, edit, dice
import random as rnd 
import numpy as np
from statistics import median

def runTesting(testPercent, n_samples):
    samples_accuracy = []
    for n_sample in range(n_samples):
        ret = loadXMLandDivideVali('./data/KB.xml', .20)
        KB = ret[0]
        test = ret[1]

        # TODO: preprocess KB
        preprocessing = combination # TODO:
        k = 0
        for question in KB:
            KB[k,0] = preprocessing(question[0])
            k+=1

        # TODO: add functions of preprocessing and similarity
        resultsList = processTest(
            KB, 
            test[:,0], 
            preprocessing, # preprocessing
            jaccard # similarity
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
        samples_accuracy.append(correct/test.shape[0])
        #print(correct)
        #print(wrong)
        #print('Test Accuracy: ' + str(correct/test.shape[0]))
        print(str(n_sample+1) + " done with " + str(correct/test.shape[0]))

    #Get average accuracy
    print('Median Test Accuracy given ' + str(n_samples) + ' samples: ' + 
        str(median(samples_accuracy))
    )

def runTestingWithDesen():
    KB = np.load("./data/KB.npy")
    vali = np.load("./data/desen.npy")
    # preprocess KB
    preproc = lambda x: combination(x)
    func = np.vectorize(preproc)
    KB[:,0] = func(KB[:,0])

    # TODO: add functions of preprocessing and similarity
    resultsList = processTest(
        KB, 
        vali[:,0], 
        preproc, # preprocessing
        dice # similarity
    )

    # TODO: get measures
    correct = 0
    wrong = 0
    k = 0
    for result in resultsList:
        if result == vali[k,1]:
            correct += 1
        wrong += 1
        k += 1
    print(correct/vali.shape[0])
        

runTestingWithDesen()