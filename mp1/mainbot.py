from preprocessing import remove_new_line
import math
from threading import Thread
import numpy as np
import statistics

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
        #TODO: add threading here (divide KB into 4)
        
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
        # write to results file
        results.write(str(best_question_id) + '\n') 
        # append to results list
        resultsList.append(best_question_id)
    results.close()
    return resultsList

# mean 0.95
# median 0.91
# harmonic_mean 0.95
# median_low 0.89
# median_high 0.91
# median grouped 1 .44