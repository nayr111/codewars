def digital_root(n):
    # first, split the digits into individual numbers, add the together, and do the same
    # over and over.
    # do so until the final number is 1 digit.
    while n >= 10: 
        digits = list(map(int, str(n))) # 123 -> [1, 2, 3]
        n = sum(digits)
    return n
