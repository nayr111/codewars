def get_count(sentence):
    vowels = ['a', 'e', 'i', 'o', 'u']
    return sum(1 for vowel in sentence if vowel in vowels)
