import re

def combination(question):
    """
    One possible combination of preprocessing techniques to use.
    """
    question = re.sub(u"ã", 'a', question)
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
    question = re.sub(u"Á", "A", question)
    question = re.sub(u"À", "A", question)
    question = re.sub(u"Õ", "O", question)
    question = re.sub(u"Ô", "O", question)
    question = re.sub(u"Ô", "O", question)
    question = re.sub(u"Ó", 'O', question)
    question = re.sub(u"Í", "I", question)
    question = re.sub(u"Ú", "U", question)
    question = re.sub(u"Ç", "C", question)
    question = re.sub(u"É", "E", question)
    return remove_leading_trailing_whitespace(
            remove_new_line(
            remove_punctuation(
            all_lowercase(
                question
            )))
    )

def remove_new_line(question):
    """
    Remove new lines from questions since some questions in KB have too
    many lines
    """
    return question.replace('\n','')
    
def remove_leading_trailing_whitespace(question):
    """
    Remove leading and trailing whitespace.
    """
    return question.strip().lstrip()

def remove_punctuation(question):
    """
    Remove punctuation from a question.
    """
    return re.sub(r"[?|\.|!|:|,|;]", '', question)

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

def remove_stopwords(question):
    """
    Remove stopwords 
    """
    pass

# taken from https://gist.github.com/alopes/5358189
STOPWORDS = ["de","a","o","que","e","do","da","em","um","para","é","com","não","uma","os","no","se","na","por","mais","as","dos","como","mas","foi","ao","ele","das","tem","à","seu","sua","ou","ser","quando","muito","há","nos","já","está","eu","também","só","pelo","pela","até","isso","ela","entre","era","depois","sem","mesmo","aos","ter","seus","quem","nas","me","esse","eles","estão","você","tinha","foram","essa","num","nem","suas","meu","às","minha","têm","numa","pelos","elas","havia","seja","qual","será","nós","tenho","lhe","deles","essas","esses","pelas","este","fosse","dele","tu","te","vocês","vos","lhes","meus","minhas","teu","tua","teus","tuas","nosso","nossa","nossos","nossas","dela","delas","esta","estes","estas","aquele","aquela","aqueles","aquelas","isto","aquilo","estou","está","estamos","estão","estive","esteve","estivemos","estiveram","estava","estávamos","estavam","estivera","estivéramos","esteja","estejamos","estejam","estivesse","estivéssemos","estivessem","estiver","estivermos","estiverem","hei","há","havemos","hão","houve","houvemos","houveram","houvera","houvéramos","haja","hajamos","hajam","houvesse","houvéssemos","houvessem","houver","houvermos","houverem","houverei","houverá","houveremos","houverão","houveria","houveríamos","houveriam","sou","somos","são","era","éramos","eram","fui","foi","fomos","foram","fora","fôramos","seja","sejamos","sejam","fosse","fôssemos","fossem","for","formos","forem","serei","será","seremos","serão","seria","seríamos","seriam","tenho","tem","temos","tém","tinha","tínhamos","tinham","tive","teve","tivemos","tiveram","tivera","tivéramos","tenha","tenhamos","tenham","tivesse","tivéssemos","tivessem","tiver","tivermos","tiverem","terei","terá","teremos","terão","teria","teríamos","teriam"]