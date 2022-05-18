'''
Exercise 18: retreiving the last line of a file
'''

def last_line_old(filename):
    '''
    Return a string containing the last line of a file.
    If problems, return empty string.
    '''
    res = ''
    try:
        with open(filename) as myfile:
            res = myfile.readline()
            tmp = myfile.readline()
            while tmp != '':
                tmp = myfile.readline()
                if tmp:
                    res = tmp
    except FileNotFoundError:
        res = 'file-not-found'
    return res
#---


def last_line(filename):
    '''
    Return a string containing the last line of a file,
    exploiting the fact that local for variables are NOT
    destroyed after exiting the loop
    (differently from C/C++)
    '''
    res = ''
    try:
        with open(filename) as myfile:
            for current_line in myfile:
                pass
            res = current_line
    except FileNotFoundError:
        res = 'FILE-NOT-FOUND'
    return res
#---


if __name__ == '__main__':
    print(last_line("prova_non_esistente.txt"))
    print(last_line("dummy_file.txt"))
