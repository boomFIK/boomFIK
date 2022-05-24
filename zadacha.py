one = {'a': 1, 'b': 2}
two = {'c': 3}
def merge_dict(d_one, d_two):
    merged = {}
    for i in d_one:
        if i in d_two:
            megred[i] = [d_one[i], d_two[i]]
        else:
            merged[i] = d_one[i]
    for i in d_two:
        if i not in d_one:
            merged[i] = d_two[i]
    return merged 

    



