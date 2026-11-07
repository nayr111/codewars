def move_zeros(lst):
    target = 0
    newlist = [x for x in lst if x != target] + [x for x in lst if x == target]
    return newlist
