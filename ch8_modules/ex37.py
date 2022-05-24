'''
Using a bit the menu developed in the corresponding module.
'''
from menu import menu

def fun_a():
    '''
    Example
    '''
    return 'fun_a'
#---

def fun_b():
    '''
    Example
    '''
    return 'fun_b'
#---

def fun_c():
    '''
    Example
    '''
    return 'fun_c'
#---


if __name__ == '__main__':
    print(menu(a=fun_a, b=fun_b))
