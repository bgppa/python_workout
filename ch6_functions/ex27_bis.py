'''
Basically a clone of itemgetter.
'''

def getitem(index):
    '''
    Return a function to extract the nth element.
    '''
    def extract(assume_valid_sequence):
        '''
        Take a sequence and return the _index_ element
        of the sequence.
        '''
        return assume_valid_sequence[index]
    #---
    return extract
#---


if __name__ == '__main__':
    tmp = getitem(4)
    print(tmp("ciaociao"))
    print(tmp({'d':3, 4:'hello!'}))
