import math
from threading import Thread
import numpy as np
import statistics

# THRESHOLD FOR JACCARD/DICE
THRESHOLD = 0.6

def processTest(KB, test, preprocessing, similarity):
    """
    Receive a KB and test set, and using the preprocessing and 
    similarity functions given, process the test set using a retrieval 
    based method with KB as the knowledge base.
    Results are returned in a list and written to a file resultados.txt.
    """

    results = open('resultados.txt', "w+")
    resultsList = []
    for test_question in test:
        # preprocess test question
        preproc_question = preprocessing(test_question)

        best_question_id = -1
        best_similarity_value = math.inf
        for k in range(KB.shape[0]):
            value = similarity(KB[k,0], preproc_question)
            if value < best_similarity_value:
                best_question_id = KB[k,1]
                best_similarity_value = value
        # threshold
        if similarity.__name__ != 'edit' and best_similarity_value > THRESHOLD:
            best_question_id = '0'
        # write to results file
        results.write(best_question_id + '\n') 
        # append to results list
        resultsList.append(best_question_id)
    results.close()
    return resultsList


def processTestGrouping(KB, test, preprocessing, similarity):
    """
    Receive a KB and test set, and using the preprocessing and 
    similarity functions given, process the test set using a retrieval 
    based method with KB as the knowledge base.
    Results are returned in a list and written to a file resultados.txt.
    """

    results = open('resultados.txt', "w+")
    resultsList = []
    for test_question in test:
        # preprocess test question
        preproc_question = preprocessing(test_question)        
        # set values for finding max
        best_question_id = -1
        best_similarity_value = math.inf
        # loop retrieval and similarity assessment
        a_id = KB[0,1]
        similarity_faq = []
        for kb_question in KB:
            if kb_question[1] != a_id:
                stat = statistics.harmonic_mean(similarity_faq)
                if stat < best_similarity_value:
                    best_question_id =  a_id
                    best_similarity_value = stat
                a_id = kb_question[1]
                similarity_faq = []

            value = similarity(kb_question[0], preproc_question)
            similarity_faq.append(value)
        
        # last one
        stat = statistics.harmonic_mean(similarity_faq)
        if stat < best_similarity_value:
            best_question_id =  a_id
            best_similarity_value = stat
        # threshold
        if similarity.__name__ != 'edit' and best_similarity_value > THRESHOLD:
            best_question_id = '0'
        # write to results file
        results.write(str(best_question_id) + '\n') 
        # append to results list
        resultsList.append(best_question_id)
    results.close()
    return resultsList

# GROUP
# mean 0.919
# median 0.878 1by1 91.1
# harmonic_mean 93.5 91.1
# median_low 0.86 91.1
# median_high 86.2 91.1
# median grouped-1 .44