'''
Another exercise on comprehension and filtering.
'''

def sum_numbers(string_of_numbers):
    '''
    Take in input a string.
    Split into words, and sum all the numbers.
    Ignore the remainings.
    '''
    tmp = string_of_numbers.strip().split()
    return sum(int(number) for number in tmp if number.isdigit())
#---


if __name__ == '__main__':
    print(sum_numbers("10 abc 20 de44 30 55fg 40 xx"))
