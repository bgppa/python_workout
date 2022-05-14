'''
Sorting a string
'''

def strsort (word):
    '''
    Simply sort a string. Trivial, but essential to remember
    '''
    return ''.join(sorted(word))
#---


if __name__ == '__main__':
    user_in = 'ok'
    while len(user_in) > 0:
        user_in = input('Enter a string to sort: ')
        if len(user_in) > 0:
            print(strsort(user_in))
