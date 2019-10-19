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
    return (2*(len(string1.intersection(string2)))) / (len(string1)+len(string2))
        

def edit(string1, string2):
    '''
    Edit distance
    '''
    return edit_distance(
        string1.split(),
        string2.split()
    )