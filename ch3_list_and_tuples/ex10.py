'''
Exercise 10: writing a generalied sum function
'''

def mysum (*args):
    '''
    Just return the sums of all the passed arguments
    '''
    # if the argument list is empy, return an empty list
    if not args:
        return []
    # else, sum all the elements
    tot = args[0]
    for elm in args[1:]:
        tot += elm
    return tot
#---


def sum_numeric (*args):
    '''
    sum all the arguments that can be converted into a number
    '''
    if not args:
        return 0.
    tot = 0.
    for elm in args:
        try:
            float(elm)
        except (ValueError, TypeError) as err:
            # simply ignore the value
            pass
        else:
            tot += float(elm)
    return tot
#---

if __name__ == '__main__':
    print(mysum(1, 2, 3))
    print(mysum([1], [2], [3]))
    print(mysum(*[1, 2, 3]))
    print(mysum("ciao", " chi ", "sei?"))
    print(sum_numeric())
    print(sum_numeric(*[10, 20, "-31", "ciao"]))
    print(sum_numeric([10, 20, "-31", "ciao"]))
