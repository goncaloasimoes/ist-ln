import argparse
from KB import loadXML
from preprocessing import combination3
from similarity import dice
from mainbot import processTestGrouping
import random as rnd
import numpy as np

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
    # Default, Stemming, Stopwords
    preprocessing = combination3 
    func = np.vectorize(preprocessing)
    KB[:,0] = func(KB[:,0])
    
    # Load questions in test into list
    test = []
    with open(args.test, 'r') as f:
        test = f.readlines()
    test = [question.strip() for question in test]

    # call mainbot.py
    processTestGrouping(
        KB,
        test,
        preprocessing,
        dice
    )


if __name__ == '__main__':
    main()