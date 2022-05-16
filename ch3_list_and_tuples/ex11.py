'''
Exercise 11: Alphabetizing names
The point of this exercise is to familiarize with the key argument of sorted
'''
PEOPLE = [{'first' : 'Reuven', 'last' : 'Lerner', 'email' : 'fjfj'},
            {'first' : 'Donald', 'last' : 'Trump', 'email' : 'sjsj'},
            {'first' : 'Vladimir', 'last' : 'Putin', 'email' : 'ed'}]

def alphabetize_names ():
    '''
    Return a sorted version of PEOPLE
    '''
    return sorted(PEOPLE, key = lambda x : x['first'])
#---


if __name__ == '__main__':
    print(PEOPLE)
    print("Sorted: ")
    print(alphabetize_names())
