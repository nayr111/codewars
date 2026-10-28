# using 123 as an example
def square_digits(num):
    numlist = [int(x) for x in str(num)] # 123 -> [1, 2, 3]
    factor = 2
    sqnumlist = [x ** factor for x in numlist] # [1, 2, 3] -> [1, 4, 9]
    strnumlist = [str(x) for x in sqnumlist] # [1, 4, 9] -> ['1', '4', '9']
    stringnum = "".join(strnumlist) # ['1', '4', '9'] -> '149'
    result = int(stringnum) # '149' -> 149
    return result # 149
