from KB import loadXMLandDivideVali, loadXMLandDivideRandomly
from mainbot import processTest, processTestGrouping
from preprocessing import combination4, combination1, combination2, combination3, func_name_to_str
from similarity import jaccard, edit, dice
import random as rnd 
import numpy as np
import statistics
import time

def runTestingWithValidationSet():
    KB = np.load("./data/KB.npy")
    # use 
    vali = np.load("./data/desen.npy")
    preprocessing = [combination4, combination1, combination2, combination3]
    similarity = [edit, jaccard, dice]
    # preprocess KB
    copyKB = np.copy(KB)
    func = np.vectorize(combination4)
    copyKB[:,0] = func(copyKB[:,0])
    
    getNewKB = False

    # duplicates
    dupes = {}
    for i in range(copyKB.shape[0]):
        question = copyKB[i,0]
        for j in range(i+1, copyKB.shape[0]):
            if question == copyKB[j,0]:
                dupes[copyKB[i,1]] = copyKB[j,1]
                dupes[copyKB[j,1]] = copyKB[i,1]
    print(len(dupes))

    for preproc in preprocessing:
        for sim in similarity:
            if getNewKB:
                # preprocess KB
                copyKB = np.copy(KB)
                func = np.vectorize(preproc)
                copyKB[:,0] = func(copyKB[:,0])
            else:
                getNewKB = True
            
            ############
            # GROUPING #
            ############
            start = time.time()
            resultsList = processTestGrouping(
                copyKB, 
                vali[:,0], 
                preproc, # preprocessing
                sim # similarity
            )
            end = time.time() - start
            
            # Accuracy
            correct = 0
            k = 0
            for result in resultsList:
                if result == vali[k,1]:
                    correct += 1
                elif (vali[k,1] in dupes) and result == dupes[vali[k,1]]:
                    correct += 1
                k += 1
            print('Preprocessing: ' + func_name_to_str[preproc.__name__])
            print('Similarity: ' + sim.__name__)
            print('Grouping with harmonic mean:')
            print("\tAccuracy: %2.1f" % (100*correct/vali.shape[0]) + '%')
            print("\tTime: %.1f s\n" % (end))

            ###############
            # NO GROUPING #
            ###############
            start = time.time()
            resultsList = processTest(
                copyKB, 
                vali[:,0], 
                preproc, # preprocessing
                sim # similarity
            )
            end = time.time() - start

            # Accuracy
            correct = 0
            k = 0
            for result in resultsList:
                if result == vali[k,1]:
                    correct += 1
                elif (vali[k,1] in dupes) and result == dupes[vali[k,1]]:
                    correct += 1
                k += 1
            print('1 by 1 comparison')
            print("\tAccuracy: %2.1f" % (100*correct/vali.shape[0]) + '%')
            print("\tTime: %.1f s\n" % (end))

def runRandomBaseline():
    KB = np.load("./data/KB.npy")
    # use 
    vali = np.load("./data/desen.npy")
    # preprocess KB
    copyKB = np.copy(KB)
    func = np.vectorize(combination4)
    copyKB[:,0] = func(copyKB[:,0])
    # duplicates
    dupes = {}
    for i in range(copyKB.shape[0]):
        question = copyKB[i,0]
        for j in range(i+1, copyKB.shape[0]):
            if question == copyKB[j,0]:
                dupes[copyKB[i,1]] = copyKB[j,1]
                dupes[copyKB[j,1]] = copyKB[i,1]
    # get highest id
    highest = np.amax(KB[:,1].astype(int))
    accuracy_set = []
    for k in range(30):
        correct = 0
        for k in range(vali.shape[0]):
            question_id = vali[k,1]
            random_id = rnd.randint(1, highest)
            if question_id == random_id:
                correct +=1
            elif (question_id in dupes) and random_id == dupes[question_id]:
                correct += 1
        accuracy_set.append(correct/vali.shape[0])

    accuracy = statistics.mean(accuracy_set)
    print('Random baseline:')
    print('\tAccuracy: %2.1f' % (100*accuracy) + '%')

def runTestSet():
    KB = np.load("./data/KB.npy")
    # use 
    test = np.load("./data/test.npy")
    preproc = combination3
    similarity = dice

    # preprocess KB (for dupes)
    copyKB = np.copy(KB)
    func = np.vectorize(combination4) # default
    copyKB[:,0] = func(copyKB[:,0])

    # duplicates
    dupes = {}
    for i in range(copyKB.shape[0]):
        question = copyKB[i,0]
        for j in range(i+1, copyKB.shape[0]):
            if question == copyKB[j,0]:
                dupes[copyKB[i,1]] = copyKB[j,1]
                dupes[copyKB[j,1]] = copyKB[i,1]
    print(len(dupes))

    # preprocess KB with preproc
    copyKB = np.copy(KB)
    func = np.vectorize(preproc) # Default + stopwords + stem
    copyKB[:,0] = func(copyKB[:,0])

    start = time.time()
    resultsList = processTestGrouping(
        copyKB, 
        test[:,0], 
        preproc, # Default + stopwords + stem
        similarity # Dice
    )
    end = time.time() - start

    correct = 0
    k = 0
    for result in resultsList:
        if result == test[k,1]:
            correct += 1
        elif (test[k,1] in dupes) and result == dupes[test[k,1]]:
            correct += 1
        k += 1
    print('Chosen best model with test set:')
    print("\tAccuracy: %2.1f" % (100*correct/test.shape[0]) + '%')
    print("\tTime: %.1f s\n" % (end))

#runRandomBaseline()
#runTestingWithValidationSet()
runTestSet()
