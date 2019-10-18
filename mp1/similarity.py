from nltk.metrics.distance import edit_distance
from nltk.metrics.distance import jaccard_distance

def jaccard(string1, string2):
    return jaccard_distance(
        set(string1.split()),
        set(string2.split())
    )
        

def edit(string1, string2):
    return edit_distance(
        string1.split(),
        string2.split()
    )