def count_bits(n):
    # convert the integer to binary
    # check how many 1's appear in the binary
    # return the total amount of 1's in the binary
    
    binary = format(n, "b") # 1234 -> '10011010010'
    target = 1
    result = binary.count(str(target)) # '10011010010' -> 5
    return result
