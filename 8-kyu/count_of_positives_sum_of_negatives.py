def count_positives_sum_negatives(arr):
    if not arr:
        return []
    len_of_pos = len([i for i in arr if i > 0])
    sum_of_neg = sum(i for i in arr if i < 0)
    return [len_of_pos, sum_of_neg]
