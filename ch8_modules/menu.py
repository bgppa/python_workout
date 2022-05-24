'''
Just writing a menu.
'''

def menu(**kwargs):
    '''
    Create an interface such that, by entering a string (key),
    the corresponding value will be called.
    Keys are assumed to be strings, values to be functions.
    '''
    while True:
        print(f"Available functions: {kwargs.keys()}")
        user_in = input("Choose which function to run: ")
        # if valid input, return the value of the called function
        if user_in in kwargs:
            return kwargs[user_in]()
        # if not valid, repeat if user didn't write ENTER
        if user_in:
            print("Value not found. Try again")
        # otherwise just end
        else:
            return 0
#---
