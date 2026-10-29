def filter_list(l):
    filtered = [i for i in l if type(i) is not str]
    return filtered
