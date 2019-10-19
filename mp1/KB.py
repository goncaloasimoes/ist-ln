import xml.etree.ElementTree as ET
import numpy as np
import random as rnd
from preprocessing import remove_new_line, remove_leading_trailing_whitespace

def loadXML(filepath):
    """
    Given a path to a xml file, load that file as a numpy array 
    containing rows of question and its answer id.
    """

    # get root of xml
    root = ET.parse(filepath).getroot()

    # base list of list pairs of [question, answer id]
    questions = []

    i = 0
    # Get every set of questions and answer
    for faq in root.iter('faq'):
        # get answer
        answer = faq.findall('resposta')[0]

        # get answer id
        id = answer.attrib['id']

        # loop on all questions on this faq set
        for question in faq.iter('pergunta'):
            if len(question.text.strip()) == 0:
                continue
            # add to questions list
            questions.append([question.text, id])
        i += 1

    # get numpy array KB given questions list
    KB = np.asarray(questions)

    return KB

def loadXMLandDivideVali(filepath, valiPercent):
    """
    Given a path to a xml file, return KB and vali arrays containing
    questions-answers sets, where the vali set is achieved by removing 
    valiPercent of the questions.
    """

    # get root of xml
    root = ET.parse(filepath).getroot()

    # base list of list pairs of [[questions], answer id]
    questions = []

    i = 0
    # Get every set of questions and answer
    for faq in root.iter('faq'):
        # get answer
        answer = faq.findall('resposta')[0]

        # get answer id
        id = answer.attrib['id']

        aux_questions = []
        # loop on all questions on this faq set
        for question in faq.iter('pergunta'):
            if len(question.text.strip()) == 0:
                continue
            # add to questions list
            aux_questions.append(question.text)
        questions.append([aux_questions, id])
        i += 1

    vali = []
    # Get sample of questions-answers sets to remove using valiPercent
    size = len(questions)
    toRemove = rnd.sample(range(size), int(size*valiPercent))
    faqWith1Question = 0
    for idxSet in toRemove:
        faqSet = questions[idxSet]
        questionsRemove = faqSet[0]
        if len(questionsRemove) == 1:
            faqWith1Question +=1
            continue
        choice = rnd.choice(range(len(questionsRemove)))
        vali.append([questionsRemove[choice], faqSet[1]])
        del questionsRemove[choice]
    print('Question with one skipped: ' + str(faqWith1Question))
    testArray = np.asarray(vali)

    KB = []
    for faqSet in questions:
        id = faqSet[1]
        for question in faqSet[0]:
            KB.append([question, id])
    # get numpy array KB given questions list
    KB = np.asarray(KB)

    return [KB, testArray]

def loadXMLandDivideRandomly(filepath, valiPercent):
    """
    Given a path to a xml file, return KB and vali arrays containing
    questions-answers sets, where the vali set is achieved by removing 
    one question per questions-answer sets given a valiPercent random 
    choice of sets to remove from.
    """

    # get root of xml
    root = ET.parse(filepath).getroot()

    # base list of list pairs of [question, answer id]
    questions = []

    i = 0
    # Get every set of questions and answer
    for faq in root.iter('faq'):
        # get answer
        answer = faq.findall('resposta')[0]

        # get answer id
        id = answer.attrib['id']

        # loop on all questions on this faq set
        for question in faq.iter('pergunta'):
            if len(question.text.strip()) == 0:
                continue
            # add to questions list
            questions.append([question.text, id])
        i += 1

    vali = []
    # Get sample of questions-answers sets to remove using valiPercent
    size = len(questions)
    toRemove = rnd.sample(range(size), int(size*valiPercent))
    toRemove.sort()
    k = 0
    for idxSet in toRemove:
        questionToRemove = questions[idxSet-k]
        vali.append(questionToRemove)
        del questions[idxSet-k]
        k +=1
    testArray = np.asarray(vali)

    KB = np.asarray(questions)

    return [KB, testArray]


def loadXMLandDivideTestValidation(filepath, valiPercent, testPercent):
    """
    
    """
    # get root of xml
    root = ET.parse(filepath).getroot()

    # base list of list pairs of [[questions], answer id]
    questions = []

    i = 0
    # Get every set of questions and answer
    for faq in root.iter('faq'):
        # get answer
        answer = faq.findall('resposta')[0]

        # get answer id
        id = answer.attrib['id']

        aux_questions = []
        # loop on all questions on this faq set
        for question in faq.iter('pergunta'):
            if len(question.text.strip()) == 0:
                continue
            # add to questions list
            aux_questions.append(question.text)
        questions.append([aux_questions, id])
        i += 1

    KBSIZE = len(questions)
    test = []
    # Get sample of questions-answers sets to remove using testPercent
    toRemove = rnd.sample(range(KBSIZE), int(KBSIZE*testPercent))
    faqWith1Question = 0
    for idxSet in toRemove:
        faqSet = questions[idxSet]
        questionsRemove = faqSet[0]
        if len(questionsRemove) == 1:
            faqWith1Question +=1
            continue
        choice = rnd.choice(range(len(questionsRemove)))
        test.append([questionsRemove[choice], faqSet[1]])
        del questionsRemove[choice]
    print('Question with one skipped: ' + str(faqWith1Question))
    testArray = np.asarray(test)

    vali = []
    # Get sample of questions-answers sets to remove using valiPercent
    toRemove = rnd.sample(range(KBSIZE), int(KBSIZE*valiPercent))
    faqWith1Question = 0
    for idxSet in toRemove:
        faqSet = questions[idxSet]
        questionsRemove = faqSet[0]
        if len(questionsRemove) == 1:
            faqWith1Question +=1
            continue
        choice = rnd.choice(range(len(questionsRemove)))
        vali.append([questionsRemove[choice], faqSet[1]])
        del questionsRemove[choice]
    print('Question with one skipped: ' + str(faqWith1Question))
    valiArray = np.asarray(vali)

    KB = []
    for faqSet in questions:
        id = faqSet[1]
        for question in faqSet[0]:
            KB.append([question, id])
    # get numpy array KB given questions list
    KB = np.asarray(KB)

    return [KB, valiArray, testArray]

# KB = loadXML('./data/KB.xml')
# ret = loadXMLandDivideTest('./data/KB.xml', 0.30)
# ret2 = loadXMLandDivideRandomly('./data/KB.xml', 0.30)
# KB2 = ret[0]
# testArray2 = ret[1]
# KB3 = ret2[0]
# testArray3 = ret2[1]
# print(KB.shape)
# print(KB2.shape)
# print(testArray2.shape)
# print(KB2.shape[0] + testArray2.shape[0])

# print(KB3.shape)
# print(testArray3.shape)
# print(KB3.shape[0] + testArray3.shape[0])



def save_KB_vali_test():
    ret = loadXMLandDivideTestValidation('./data/KB.xml', .2, .1)
    KB = ret[0]
    vali = ret[1]
    test = ret[2]
    np.save("./data/KB", KB)
    np.save("./data/desen", vali)
    np.save("./data/test", test)

    # KBread = np.load("./data/KB.npy")
    # valiread = np.load("./data/desen.npy")
    # testread = np.load("./data/test.npy")
