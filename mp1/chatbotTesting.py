from KB import loadXMLandDivideVali, loadXMLandDivideRandomly
from mainbot import processTest, processTestNoThreads
from preprocessing import combination3
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
        preprocessing = combination3 # TODO:
        k = 0
        for question in KB:
            KB[k,0] = preprocessing(question[0])
            k+=1

        # TODO: add functions of preprocessing and similarity
        resultsList = processTest(
            KB, 
            test[:,0], 
            preprocessing, # preprocessing
            dice # similarity
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

def runTestingWithValidationSet():
    KB = np.load("./data/KB.npy")
    vali = np.load("./data/desen.npy")
    # preprocess KB
    preproc = lambda x: combination3(x)
    func = np.vectorize(preproc)
    KB[:,0] = func(KB[:,0])

    # duplicates
    dupes = {}
    for i in range(KB.shape[0]):
        question = KB[i,0]
        for j in range(KB.shape[0]):
            if i == j:
                continue
            if question == KB[j,0]:
                dupes[KB[i,1]] = KB[j,1]
                dupes[KB[j,1]] = KB[i,1]


    # print(KB.shape)
    # aux = np.unique(KB[:,0],return_index=True, return_inverse=True)
    # print(aux[2].shape)
    # KB = KB[aux[1]]
    #print(new.shape)
    # u, c = np.unique(KB[:,0], return_counts=True)
    # dup = u[c > 1]
    # print(dup.shape)
        
    
    # TODO: add functions of preprocessing and similarity
    resultsList = processTestNoThreads(
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
        elif (vali[k,1] in dupes) and result == dupes[vali[k,1]]:
            correct += 1
        else:
            print(vali[k,0],vali[k,1])
            print(preproc(vali[k,0]))
            print(KB[KB[:,1] == result][0])
            print('\n')
            wrong += 1
        k += 1
    print(correct/vali.shape[0])

  

runTestingWithValidationSet()
