def find_it(seq):
    #check how many times a number appears in the list
    #if the number appears an odd amount of times, return it
    for i in seq:
        if seq.count(i) % 2 == 1:
            return i
