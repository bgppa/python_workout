'''
Exercise 13: Printing tuple records.
This is just to revise the use of print f string format.
'''
PEOPLE = [('Donald', 'Trump', 7.85),
            ('Vladimir', 'Putin', 3.626),
            ('Jinping', 'Xi', 10.603)]

def format_sort_records ():
    '''
    I: nothing, it acts on the global variable PEOPLE
    O: 1; it just displays PEOPLE in a formatted way
    '''
    for record in PEOPLE:
        print(f"{record[1]:10s}{record[0]:10s}{record[2]:.2f}")
    return 1
#---

if __name__ == '__main__':
    format_sort_records()
