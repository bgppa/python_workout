'''
Exercise 26: Prefix notation calculator.
'''
import operator

def operation(opval):
    '''
    Convert a char into a valid arithmetic operation.
    '''
    res = {'+' : operator.add, '-':operator.sub, '*':operator.mul,
            '/':operator.floordiv}
    if opval in res:
        return res[opval]

    print("Operation not valid")
    return lambda x, y : 0
#---

def calc_old(pnotation):
    '''
    pnotation is expected to be a string of the form
    "OP a b" there OP is a valid aritmetic operation.
    '''
    formatted = pnotation.strip().split()
    return operation(formatted[0])(int(formatted[1]), int(formatted[2]))
#---


def calc(pnotation):
    '''
    This time allow iterated operations.
    '''
    tmp = pnotation.strip().split()
    op_chosen = operation(tmp[0])
    res = op_chosen(int(tmp[1]), int(tmp[2]))

    # iterating now on the remaining arguments
    for nth in range(len(tmp) - 3):
        res = op_chosen(res, int(tmp[nth + 3]))
    return res
#---


if __name__ == '__main__':
    exp1 = "+ 2 3"
    exp2 = "% 2 3"
    exp3 = "*    23 1"
    exp4 = "+   3 5 7 "
    exp5 = "/ 100 5 5 "
    exp6 = "+ 1 2 3 4 5 6"
    print(f"{exp1} = {calc(exp1)}")
    print(f"{exp2} = {calc(exp2)}")
    print(f"{exp3} = {calc(exp3)}")
    print(f"{exp4} = {calc(exp4)}")
    print(f"{exp5} = {calc(exp5)}")
    print(f"{exp6} = {calc(exp6)}")
