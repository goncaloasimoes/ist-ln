
def remove_new_line(question):
    """
    Remove new lines from questions since some questions in KB have too
    many lines
    """
    return question.replace('\n','')
    