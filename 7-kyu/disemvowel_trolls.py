def disemvowel(string_):
    vowels = "aeiouAEIOU"
    newstring = string_
    for vowel in vowels:
        newstring = newstring.replace(vowel, "")
    return newstring
