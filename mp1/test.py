import xml.etree.ElementTree as ET
import numpy as np
import random as rnd


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
            # add to questions list
            questions.append([question.text, id])
        i += 1

    # get numpy array KB given questions list
    KB = np.asarray(questions)

    return KB

def loadXMLandDivideTest(filepath, testPercent):
    """
    Given a path to a xml file, return KB and test arrays containing
    questions-answers sets, where the test set is achieved by removing 
    one question per questions-answer sets given a testPercent random 
    choice of sets to remove from.
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
            # add to questions list
            aux_questions.append(question.text)
        questions.append([aux_questions, id])
        i += 1

    test = []
    # Get sample of questions-answers sets to remove using testPercent
    size = len(questions)
    toRemove = rnd.sample(range(size), int(size*testPercent))
    for idxSet in toRemove:
        faqSet = questions[idxSet]
        questionsRemove = faqSet[0]
        choice = rnd.choice(range(len(questionsRemove)))
        test.append([questionsRemove[choice], faqSet[1]])
        del questionsRemove[choice]
    testArray = np.asarray(test)

    KB = []
    for faqSet in questions:
        id = faqSet[1]
        for question in faqSet[0]:
            KB.append([question, id])
    # get numpy array KB given questions list
    KB = np.asarray(KB)

    return [KB, testArray]

KB = loadXML('./data/KB.xml')
ret = loadXMLandDivideTest('./data/KB.xml', 0.20)
KB2 = ret[0]
testArray = ret[1]
print(KB.shape)
print(KB2.shape)
print(testArray.shape)
print(KB2.shape[0] + testArray.shape[0])
