def reverse_words(s):
    words = s.split()
    revwords = words[::-1]
    return " ".join(revwords)
