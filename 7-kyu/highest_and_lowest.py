def high_and_low(numbers):
    strlist = numbers.split() # "1 2 3 4 5" -> ['1', '2', '3', '4', '5']
    intlist = [int(x) for x in strlist] # ['1', '2', '3', '4', '5'] -> [1, 2, 3, 4, 5]
    maxval = max(intlist) # 5
    minval = min(intlist) # 1
    max_minlist = [maxval, minval] # [5, 1]
    newlist = [str(x) for x in max_minlist] # ['5', '1']
    result = str(" ".join(newlist)) # '5 1'
    return result
