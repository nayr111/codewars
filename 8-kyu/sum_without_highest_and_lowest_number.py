def sum_array(arr):
    if not arr or len(arr) < 3:
        return 0
    elif len(arr) >= 3:
        return sum(arr) - (min(arr) + max(arr))
    else:
        return 0
