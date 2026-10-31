def spin_words(sentence):
    #first we turn the word or sentence into a list
    #then we check for if a word has 5 or more letters. if len(word) >= 5
    #then if the length of the word is greater than 5, we reverse it.
    #if not, return it as usual.
    
    slist = sentence.split() # ['Welcome']
    check = [word[::-1] if len(word) >= 5 else word for word in slist]
    return " ".join(check)
    
