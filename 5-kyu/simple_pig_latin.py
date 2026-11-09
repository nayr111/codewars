def pig_it(text):
    original = [word for word in text.split()] # Hello World -> ["Hello", "World"]
    first_letters = [word[0] for word in text.split()] # Hello World -> ["H", "W"]
    ay = [word + "ay" for word in first_letters] # ["H", "W"] -> ["Hay", "Way"]
    combined = [w1[1:] + w2 if w1.isalpha() else w1 for w1, w2 in zip(original, ay)] # ["elloHay", "orldWay"]
    result = " ".join(combined) # 'elloHay orldWay'
    return result
