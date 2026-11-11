# hardcoded for 3x3 arrays only, used as test to see how i could approach the kata.
def snail(snail_map):
    lst = []
    lst.extend(snail_map[0]) # [1, 2, 3]
    lst.append(snail_map[1][-1]) # [1, 2, 3, 6]
    lst.extend(snail_map[2][::-1]) # [1, 2, 3, 6, 9, 8, 7]
    lst.append(snail_map[1][0]) # [1, 2, 3, 6, 9, 8, 7, 4]
    lst.append(snail_map[1][1]) # [1, 2, 3, 6, 9, 8, 7, 4, 5]
    return lst
