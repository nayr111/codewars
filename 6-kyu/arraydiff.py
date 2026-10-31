def array_diff(a, b):
    #check if the 1st list has any elements from the 2nd list
    #if so, remove all instances of them
    #the result shall be the 1st list without the elements of the 2nd list
    filter = [i for i in a if i not in b]
    return filter
