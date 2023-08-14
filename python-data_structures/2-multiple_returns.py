def multiple_returns(sentence):
    length = len(sentence)
    if len(sentence) == 0:
        first = None
    else:
        first = sentence[0]
    
    return len(sentence), first
