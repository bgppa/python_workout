'''
Exercise 7: the Ubbi Dubbi translator
'''

def ubbi_dubbi (word):
    '''
    Translate a single word into ubbi dubbi equivalent
    I: word, a string
    O: a string intended as the translation
    '''
    as_list = []
    for char in word:
        if char in 'aeiou':
            as_list.append('ub')
        as_list.append(char)

    result = ''.join(as_list)
    return result
#---


if __name__ == '__main__':
    user_input = 'ok'
    while len(user_input) > 0:
        user_input = input("Enter a word to translate: ")
        if len(user_input) > 0:
            print(ubbi_dubbi(user_input))
