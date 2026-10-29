def is_isogram(string):
    if len(string.lower()) != len(set(string.lower())):
        return False
    else:
        return True
   
