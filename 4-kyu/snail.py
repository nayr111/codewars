def snail(snail_map):
    lst = []
    while snail_map:
        lst.extend(snail_map.pop(0)) # [1, 2, 3]
        for row in snail_map:
            if row:
                lst.append(row.pop()) # [1, 2, 3, 6]
        if snail_map:
            lst.extend(snail_map.pop()[::-1]) # [1, 2, 3, 6, 9, 8, 7]
        for row in reversed(snail_map):
            if row:
                lst.append(row.pop(0)) # [1, 2, 3, 6, 9, 8, 7, 4]
        # repeats while loop until grid is empty [1, 2, 3, 6, 9, 8, 7, 4, 5]
    return lst
