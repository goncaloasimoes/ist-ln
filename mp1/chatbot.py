import argparse
from KB import loadXML

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
    # Load questions in test into list
    # call mainbot.py


if __name__ == '__main__':
    main()