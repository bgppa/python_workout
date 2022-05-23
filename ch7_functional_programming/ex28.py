'''
A trivial exercise for comprehensions - expression generators.
'''
import random

def join_numbers(range_of_integers):
    '''
    Take a _range_ of integers and return a string swhowing them
    separated by commas.
    '''
    return ", ".join(str(num) for num in range_of_integers if num < 10)
#---

if __name__ == '__main__':
    for nth in range(0, 10):
        chosen = random.randint(4, 15)
        print(f"[{chosen}] : {join_numbers(range(chosen))}")
