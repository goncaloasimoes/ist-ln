from KB import loadXMLandDivideVali, loadXMLandDivideRandomly
from mainbot import processTest, processTestGrouping
from preprocessing import combination4, combination1, combination2, combination3, func_name_to_str
from similarity import jaccard, edit, dice
import random as rnd 
import numpy as np
import statistics
import time

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
        str(statistics.median(samples_accuracy))
    )

def runTestingWithValidationSet():
    KB = np.load("./data/KB.npy")
    # use 
    vali = np.load("./data/desen.npy")
    preprocessing = [combination4, combination1, combination2, combination3]
    similarity = [edit, jaccard, dice]
    # preprocess KB
    copyKB = np.copy(KB)
    func = np.vectorize(preprocessing[0])
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
            print('DUPES:'+str(len(dupes)))
            
            # print(KB.shape)
            # aux = np.unique(KB[:,0],return_index=True, return_inverse=True)
            # print(aux[2].shape)
            # KB = KB[aux[1]]
            # print(new.shape)
            # u, c = np.unique(KB[:,0], return_counts=True)
            # dup = u[c > 1]
            # print(dup.shape)
                
            ############
            # GROUPING #
            ############
            start = time.time()
            # TODO: add functions of preprocessing and similarity
            resultsList = processTestGrouping(
                copyKB, 
                vali[:,0], 
                preproc, # preprocessing
                sim # similarity
            )
            end = time.time() - start

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
                    #print(vali[k,0],vali[k,1])
                    #print(preproc(vali[k,0]))
                    #print(copyKB[copyKB[:,1] == result][0])
                    #print('\n')
                    wrong += 1
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
            # TODO: add functions of preprocessing and similarity
            resultsList = processTest(
                copyKB, 
                vali[:,0], 
                preproc, # preprocessing
                sim # similarity
            )
            end = time.time() - start

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
                    #print(vali[k,0],vali[k,1])
                    #print(preproc(vali[k,0]))
                    #print(copyKB[copyKB[:,1] == result][0])
                    #print('\n')
                    wrong += 1
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

#runRandomBaseline()
runTestingWithValidationSet()
