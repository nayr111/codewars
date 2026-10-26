def count_positives_sum_negatives(arr):
    if not arr:
        return []
    sum_of_pos = len([i for i in arr if i > 0])
    sum_of_neg = sum(i for i in arr if i < 0)
    return [sum_of_pos, sum_of_neg]
