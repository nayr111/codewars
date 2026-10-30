def solution(number):
    #given a list of nums, find multiples of 3 and 5
    #so, i guess we can do [num for num in number if num % 3 == 0 or num % 5 == 0]
    #but first, lets turn that number into a list.
    #then we add all the numbers up, and thats our sum.
    numlist = list(range(number)) #6 -> [0, 1, 2, 3, 4, 5]
    multiples = [num for num in numlist if num % 3 == 0 or num % 5 == 0] #[0, 1, 2, 3, 4, 5] -> [3, 5]
    tsum = sum(multiples) #[3,5] -> 8
    return tsum #8
