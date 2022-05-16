'''
Exercise 9: firstlast
'''

def firstlast(iterable):
    '''
    Return the first and the last element of an interable
    '''
    if len(iterable) > 1:
        return iterable[:1] + iterable[-1:]
    print(f"Itereable too short, len: {len(iterable)}")
    return ()
#---

def even_odd_sum (list_of_nums):
    '''
    Return the sums of (even-indeces,odd_indeces) elements
    '''
    sum_even = 0
    for elm in list_of_nums[0::2]:
        sum_even += elm

    sum_odd = 0
    for elm2 in list_of_nums[1::2]:
        sum_odd += elm2

    return [sum_even] + [sum_odd]
#---

def plus_minus (list_of_nums):
    '''
    Alternate sum and subtraction in a list of values
    '''
    switch = 0
    tot = list_of_nums[0]
    for elm in list_of_nums[1:]:
        switch = (switch + 1) % 2
        if switch:
            tot += elm
        else:
            tot -= elm
    return tot
#---

def myzip (elm1, elm2):
    '''
    A simple emulator of the zip function, assuming elm1 and elm2
    are two iterators of the same lenght
    '''
    result = []
    for idx, _ in enumerate(elm1):
        result += [(elm1[idx], elm2[idx])]
    return result
#---


if __name__ == '__main__':
    print(firstlast("ciao"), firstlast(('v', 'r')), firstlast((4,)))
    print(even_odd_sum([10, 20, 30, 40, 50, 60]))
    print(plus_minus([10, 20, 30, 40, 50, 60]))
    print(myzip("ciao", [1, 2, 3, 4]))
