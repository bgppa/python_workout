'''
Exercise 17: set are mainly used to remove duplicates.
'''

def how_many_different_numbers (list_of_nums):
    '''
    Just count the amount of different numbers in a list
    '''
    return len(set(list_of_nums))
#---

if __name__ == '__main__':
    lnums = [1, 1, 2, 2, 3, 4]
    lnums2 = []
    print(how_many_different_numbers(lnums))
    print(how_many_different_numbers(lnums2))
