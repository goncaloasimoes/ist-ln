import re
import nltk
from nltk.tokenize import word_tokenize

'''
def combination(question):
    """
    One possible combination of preprocessing techniques to use.
    """
    question = remove_accents(question)

    return remove_leading_trailing_whitespace(
            remove_new_line(
            remove_punctuation(
            all_lowercase(
                question
            )))
    )
'''

func_name_to_str = {
    "combination4": 'Accents, Punctuation, lowercase all, remove parenthesis',
    "combination1": 'Accents, Punctuation, lowercase all, remove parenthesis, stopwords',
    "combination2": 'Accents, Punctuation, lowercase all, remove parenthesis, stemming',
    "combination3": 'Accents, Punctuation, lowercase all, remove parenthesis, stopwords, stemming'
}

def combination1(question):
    """
    Combining default processing with stopwords
    """
    question = default_processing(question)
    question = remove_stopwords(question, STOPWORDS)

    return question

def combination2(question):
    """
    Combining default processing with stemming
    """
    question = default_processing(question)
    question = stemming(question)

    return question

def combination3(question):
    """
    Combining default processing with stemming and stopwords
    """
    question = default_processing(question)
    question = remove_stopwords(question, STOPWORDS)
    question = stemming(question)

    return question

def combination4(question):
    """
    Combining default processing
    """
    question = default_processing(question)

    return question

def remove_new_line(question):
    """
    Removes new lines from questions since some questions in KB have too
    many lines
    """
    return question.replace('\n','')
    
def remove_leading_trailing_whitespace(question):
    """
    Removes leading and trailing whitespace.
    """
    return question.strip().lstrip()

def remove_punctuation(question):
    """
    Removes punctuation from a question.
    """
    return re.sub(r"[?|\.|!|:|,|;]", '', question)

def remove_parenthesis(question):
    """
    Removes punctuation from a question.
    """
    return re.sub(r"[(|)]", '', question)

def all_lowercase(question):
    """
    Lower case all of the string.
    """
    return question.lower()

def first_char_lowercase(question):
    """
    Lower case of only first character.
    """
    return question[0].lower() + question[1:]

def remove_stopwords(question, stopwords):
    """
    Removes stopwords
    """
    question = question.split()
    phrase = []
    for word in question:
        if word not in stopwords:
            phrase.append(word)
        question = ' '.join(phrase) #Reconstructing question

    return question

def stemming(question):
    """
    Performs stemming
    """
    stemmer = nltk.stem.RSLPStemmer()

    question = word_tokenize(question, language="portuguese")
    phrase = []
    for w in question:
        w = stemmer.stem(w)
        phrase.append(w)
    question = ' '.join(phrase)

    return question

def remove_accents(question):
    """
    Removes accents
    """
    question = re.sub(u"ã", 'a', question)
    question = re.sub(u"â", 'a', question)
    question = re.sub(u"á", "a", question)
    question = re.sub(u"à", "a", question)
    question = re.sub(u"õ", "o", question)
    question = re.sub(u"ô", "o", question)
    question = re.sub(u"ó", "o", question)
    question = re.sub(u"é", "e", question)
    question = re.sub(u"ê", "e", question)
    question = re.sub(u"í", "i", question)
    question = re.sub(u"ú", "u", question)
    question = re.sub(u"ç", "c", question)
    question = re.sub(u"Ã", 'A', question)
    question = re.sub(u"Â", 'A', question)
    question = re.sub(u"Á", "A", question)
    question = re.sub(u"À", "A", question)
    question = re.sub(u"Õ", "O", question)
    question = re.sub(u"Ô", "O", question)
    question = re.sub(u"Ò", 'O', question)
    question = re.sub(u"Ó", 'O', question)
    question = re.sub(u"Í", "I", question)
    question = re.sub(u"Ú", "U", question)
    question = re.sub(u"Ç", "C", question)
    question = re.sub(u"É", "E", question)

    return question

def default_processing(question):
    """
    Does the default processing
    """
    question = remove_accents(question)       # Removing accents
    question = remove_punctuation(question)   # Removing punctuation
    question = all_lowercase(question)        # Lowercasing
    question = remove_parenthesis(question)   # Remove parenthesis

    return question


# taken from https://gist.github.com/alopes/5358189 with some added
STOPWORDS = ["quais", "de","a","o","que","e","do","da","em","um","para","é","com","não","uma","os","no","se","na","por","mais","as","dos","como","mas","foi","ao","ele","das","tem","à","seu","sua","ou","ser","quando","muito","há","nos","já","está","eu","também","só","pelo","pela","até","isso","ela","entre","era","depois","sem","mesmo","aos","ter","seus","quem","nas","me","esse","eles","estão","você","tinha","foram","essa","num","nem","suas","meu","às","minha","têm","numa","pelos","elas","havia","seja","qual","será","nós","tenho","lhe","deles","essas","esses","pelas","este","fosse","dele","tu","te","vocês","vos","lhes","meus","minhas","teu","tua","teus","tuas","nosso","nossa","nossos","nossas","dela","delas","esta","estes","estas","aquele","aquela","aqueles","aquelas","isto","aquilo","estou","está","estamos","estão","estive","esteve","estivemos","estiveram","estava","estávamos","estavam","estivera","estivéramos","esteja","estejamos","estejam","estivesse","estivéssemos","estivessem","estiver","estivermos","estiverem","hei","há","havemos","hão","houve","houvemos","houveram","houvera","houvéramos","haja","hajamos","hajam","houvesse","houvéssemos","houvessem","houver","houvermos","houverem","houverei","houverá","houveremos","houverão","houveria","houveríamos","houveriam","sou","somos","são","era","éramos","eram","fui","foi","fomos","foram","fora","fôramos","seja","sejamos","sejam","fosse","fôssemos","fossem","for","formos","forem","serei","será","seremos","serão","seria","seríamos","seriam","tenho","tem","temos","tém","tinha","tínhamos","tinham","tive","teve","tivemos","tiveram","tivera","tivéramos","tenha","tenhamos","tenham","tivesse","tivéssemos","tivessem","tiver","tivermos","tiverem","terei","terá","teremos","terão","teria","teríamos","teriam"]
