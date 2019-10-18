
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