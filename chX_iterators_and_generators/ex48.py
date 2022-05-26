'''
Function generator for reading one line at a time,
one file at a time.
'''
import os

def for_single_file(filename):
    '''
    it returns a generator reading line-by-line the input file
    '''
    try:
        with open(filename, 'r') as myfile:
            for loc_line in myfile:
                yield loc_line
    except FileNotFoundError:
        pass
#---

def for_directory_old():
    '''
    it returns a generator,
    whose elements are generators that read the files line-by-line
    '''
    for localfile in os.listdir("./"):
        if localfile.split('.')[-1] == 'py':
            print(localfile)
            yield for_single_file(localfile)


def for_directory():
    '''
    this is the "right" solution.
    it returns a generator that read ALL files line-by-line.
    So, you have a single generator that does the full job, as required.
    Iterating in it (with a single for) gives all the complete output.
    '''
    for localfile in os.listdir("./"):
        if localfile.split('.')[-1] == 'py':
            print(localfile)
            try:
                with open(localfile, 'r') as myfile:
                    for loc_line in myfile:
                        yield loc_line
            except FileNotFoundError:
                pass
#---


if __name__ == '__main__':

    # Here we see that we can read a single file, line-by-line
    tmpf = "ex48.py"
    my_counter = 0
    for line in for_single_file(tmpf):
        print(my_counter)
        print(line)
        my_counter += 1

    # Here we read all the local files, line-by-line, but we need a DOUBLE for,
    # since we have a generator of generators
    print("Now, full exercise:")
    my_counter = 0
    for filereader in for_directory_old():
        for line in filereader:
            print(f"{my_counter} {line}")
            my_counter += 1

    # The final solution, using a single for in a single generator
    print("Definitive exercise:")
    my_counter = 0
    for line in for_directory():
        print(f"{my_counter} {line}")
        my_counter += 1
