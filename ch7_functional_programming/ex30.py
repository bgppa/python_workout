'''
Flattening a list.
'''

def flatlist (ilist):
    '''
    I: list of lists
    O: list containing all the elements, overall.
    '''
    tmp = [elm
           for sublist in ilist
           for elm in sublist]
    return tmp
#---


if __name__ == '__main__':
    print(f"{flatlist([[1, 2], [3, 4]])}")
