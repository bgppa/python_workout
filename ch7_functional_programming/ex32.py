'''
Flipping a dictionary.
'''

def dict_flip (idict):
    '''
    Return a dictionary with key-value reversed.
    '''
    return { item[1]:item[0] for item in idict.items()}
#---


if __name__ == '__main__':
    tmp1 = {'a': 1, 'b': 2, 'c' : 3}
    tmp2 = {'a': 1, 'b': 1, 'c' : 3, 'd' : 1}
    print(f"{tmp1} -> {dict_flip(tmp1)}")
    print(f"{tmp2} -> {dict_flip(tmp2)}")
