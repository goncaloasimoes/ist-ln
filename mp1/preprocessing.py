import re

def combination(question):
    """
    One possible combination of preprocessing techniques to use.
    """
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