'''
Exercise 16, on computing the differences between dictionaries.
'''

def dictdiff_old (dict1, dict2):
    '''
    Return a dictionary with the differences between dict1 and dict2
    '''
    diff = {}
    for key, value in dict1.items():
        if dict2.get(key) != value:
            diff[key] = [value, dict2.get(key)]

    for key, value in dict2.items():
        if dict1.get(key) != value:
            diff[key] = [dict1.get(key), value]

    return diff
#---


def dictdiff (dict1, dict2):
    '''
    Same as dictdiff_old, but with a more efficient approach.
    '''
    diff = {}
    # Merge all the keys avioding repetition
    # I use | as unioin between sets, while & is for intersection
    # .keys already inherit these methods, but I prefer convert into set
    # for learning purposes.
    all_keys = set(dict1.keys()) | set(dict2.keys())
    for key in all_keys:
        if dict1.get(key) != dict2.get(key):
            diff[key] = [dict1.get(key), dict2.get(key)]

    return diff
#---


if __name__ == '__main__':
    dict_1 = {'a' : 1, 'b' : 2, 'c' : 3}
    dict_2 = {'a' : 1, 'b' : 2, 'c' : 4}
    dict_3 = {'a' : 1, 'b' : 2, 'd' : 3}
    dict_4 = {'a' : 1, 'b' : 2, 'c' : 4}
    dict_5 = {'a' : 1, 'b' : 2, 'd' : 4}

    print(dictdiff(dict_1, dict_1))
    print(dictdiff(dict_1, dict_2))
    print(dictdiff(dict_3, dict_4))
    print(dictdiff(dict_1, dict_5))
