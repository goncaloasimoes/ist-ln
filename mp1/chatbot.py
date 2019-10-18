import argparse
from KB import loadXML
from preprocessing import remove_new_line, remove_leading_trailing_whitespace
from mainbot import processTest
import random as rnd

def main():
    # Deal with arguments
    parser = argparse.ArgumentParser()
    parser.add_argument(
        'kb', 
        action="store",
        type=str, 
        help='filepath to KB.xml'
    )
    parser.add_argument(
        'test', 
        action="store",
        type=str, 
        help='filepath to test.txt'
    )
    args = parser.parse_args()
    
    # load KB
    KB = loadXML(args.kb)
    
    # Preprocess KB
    #TODO: set preprocessing 
    preprocessing = lambda x: remove_leading_trailing_whitespace(
                            remove_new_line(x)
                        ) # TODO:
    k = 0
    for question in KB:
        KB[k,0] = preprocessing(question[0])
        k+=1
    
    # Load questions in test into list
    test = []
    with open(args.test, 'r') as f:
        test = f.readlines()
    test = [question.strip() for question in test]

    # call mainbot.py
    processTest(
        KB,
        test,
        lambda x: x, #TODO
        lambda x,y: rnd.randint(1,100) #TODO
    )


if __name__ == '__main__':
    main()