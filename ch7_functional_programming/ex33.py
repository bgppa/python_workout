'''
Map on a dictionary. Another very easy exercise.
'''

def transform_value(ifun, mydict):
    '''
    I: a function _ifun_ and a dictionary _mydict_
    O: a dictionary having the same keys, but values transformed by _ifun_
    '''
    return {key : ifun(val) for key, val in mydict.items()}
#---


if __name__ == '__main__':
    tmp1 = { 'a' : 1, 'b' : 2, 'c' : 3}
    print(tmp1)
    print(transform_value(lambda x : x + 1, tmp1))
