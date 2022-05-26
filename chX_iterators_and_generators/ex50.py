'''
Last exercise from the book! :)
'''

def chain(*allsequences):
    '''
    merge all the sequences into a single iterator
    '''
    for single_seq in allsequences:
        for single_elm in single_seq:
            yield single_elm
#---


if __name__ == '__main__':
    prova = chain("abc", [1,2,3], {'f' : 3, 'g': 0})
    for nth in chain(prova):
        print(nth)
