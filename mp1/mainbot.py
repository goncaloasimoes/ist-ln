from preprocessing import remove_new_line
#from similarity import
import math

def processTest(KB, test, preprocessing, similarity):
    results = open('resultados.txt', "w+")
    resultsList = []
    for test_question in test:
        # preprocess test question
        preproc_question = preprocessing(test_question)
        # set values for finding max
        best_question_id = -1
        best_similarity_value = - math.inf
        # loop retrieval and similarity assessment
        for kb_question in KB:
            value = similarity(kb_question[0], preproc_question)
            if value > best_similarity_value:
                best_question_id = kb_question[1]
                best_similarity_value = value
        # write to results file
        results.write(best_question_id + '\n') 
        # append to results list
        resultsList.append(best_question_id)
    results.close()
    return resultsList