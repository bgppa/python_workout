'''
Writing an iterator the measure which time is elapses
since the previous call
'''
import time

def itertimed(sequence):
    '''
    An function generator that keeps track of the time elapsed between
    each call.
    '''
#    old_time = time.time()
    # A better solution uses the _or_ logic function
    old_time = None
    for elm in sequence:
        new_time = time.time()

        # Now, nice shortcut: is old_time is None, the expression
        # (old_time or new_time) returns new_time and so the
        # difference is 0. It happens the first time the function is evokes.

        # if old_time is not None, use it when doing the difference.
        # it happens in all the other function calls.

        yield (new_time - (old_time or new_time), elm)
        old_time = new_time
#---


if __name__ == '__main__':
    tmp = "abcd"
    solution = itertimed(tmp)
    for nth in solution:
        print(nth)
        time.sleep(2)
