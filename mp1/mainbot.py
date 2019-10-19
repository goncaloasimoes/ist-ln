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
        #TODO: add threading here (divide KB into 4)

        # Threading preparation
        step = int(KB.shape[0]/4)
        intervals = []
        init = 0
        for k in range(4):
            if k == 3:
                intervals.append([init, KB.shape[0]-1])
            else:
                intervals.append([init, init + step])
            init = init + step + 1
        
        threads = [None] * 4
        thread_results = [None] * 4
        # Create threads
        for i in range(4):
            threads[i] = Thread(
                target=compare_kb_question, 
                args=(
                    KB,
                    preproc_question,
                    similarity,
                    intervals[i][0],
                    intervals[i][1],
                    thread_results,
                    i
                    ))
            threads[i].start()
        # Join Threads
        for i in range(4):
            threads[i].join()
        # Get best result
        thread_results = np.asarray(thread_results)
        best_id = thread_results[np.argmin(thread_results[:,1])][0]
        # write to results file
        results.write(best_id + '\n') 
        # append to results list
        resultsList.append(best_id)
    results.close()
    return resultsList


def compare_kb_question(
    KB,
    question,
    similarity,
    kb_start_index,
    kb_stop_index,
    results,
    result_index
):
    """
    """
    best_question_id = -1
    best_similarity_value = math.inf
    for k in range(kb_start_index, kb_stop_index):
        value = similarity(KB[k,0], question)
        if value < best_similarity_value:
            best_question_id = KB[k,1]
            best_similarity_value = value
    results[result_index] = [best_question_id, best_similarity_value]


def processTestNoThreads(KB, test, preprocessing, similarity):
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
                mean = statistics.median_high(similarity_faq)
                if mean < best_similarity_value:
                    best_question_id =  a_id
                    best_similarity_value = mean
                a_id = kb_question[1]
                similarity_faq = []

            value = similarity(kb_question[0], preproc_question)
            similarity_faq.append(value)
        
        # last one
        mean = statistics.median_high(similarity_faq)
        if mean < best_similarity_value:
            best_question_id =  a_id
            best_similarity_value = mean
        # write to results file
        results.write(str(best_question_id) + '\n') 
        # append to results list
        resultsList.append(best_question_id)
    results.close()
    return resultsList

# mean 0.75
# median 0.77
# harmonic_mean 0.75
# median_low 0.75
# median_high 0.80
# median grouped 1 0.34
# median grouped 2 0.11