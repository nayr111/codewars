def find_outlier(integers):
    odd = [i for i in integers if i % 2 != 0]
    even = [i for i in integers if i % 2 == 0]

    if len(odd) == 1:
        return odd[0]
    elif len(even) == 1:
        return even[0]
