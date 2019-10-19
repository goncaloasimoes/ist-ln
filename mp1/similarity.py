from nltk.metrics.distance import edit_distance
from nltk.metrics.distance import jaccard_distance

def jaccard(string1, string2):
    '''
    Jaccard distance
    '''
    return jaccard_distance(
        set(string1.split()),
        set(string2.split())
    )

def dice(string1, string2):
    '''
    Dice similarity measure
    '''
    string1 = set(string1.split())
    string2 = set(string2.split())

    lenstring1=0
    for w in string1:
        lenstring1 += len(w)
    lenstring2=0
    for w in string2:
        lenstring2 += len(w)

    return  (2*(len(string1.union(string2)) - len(string1.intersection(string2))))/(lenstring1+lenstring2)

def edit(string1, string2):
    '''
    Edit distance
    '''
    return edit_distance(
        string1.split(),
        string2.split()
    )