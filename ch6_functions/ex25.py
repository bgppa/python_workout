'''
Exercise 25: an elementary xml generator.
'''

def myxml(tagname, context = '', **kwargs):
    '''
    Return a string according to the syntax explained in the book.
    '''
    res = f"<{tagname}"
    for key, val in kwargs.items():
        res += f' {key}="{val}"'
    res += f">{context}</{tagname}>"
    return res
#---


if __name__ == '__main__':
    print(myxml('foo'))
    print(myxml('foo', 'bar'))
    print(myxml('foo', 'bar', a = 1, b = 2, c = 3))
