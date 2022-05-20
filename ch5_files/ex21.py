'''
Analyzing data from different files.
'''
import os

def longest_w_file(filename):
    '''
    Return the longest word found in a file.
    Omitting the error checking for brevity.
    '''
    res = ''
    try:
        with open(filename, 'r') as myfile:
            for line in myfile:
                for word in line.strip().split():
                    if len(word) > len(res):
                        res = word
    except (FileNotFoundError, UnicodeDecodeError) as tmp:
        print(f"Umable to read file {filename}; skipping.")

    return (res, len(res))
#---


def all_longest(directory):
    '''
    Scan a directory and return a dictionary of shape
    filename : longest word
    '''
    res = {}
    for afile in os.listdir(directory):
        res[afile] = longest_w_file(afile)

    return res
#---


if __name__ == '__main__':
    print(f"{longest_w_file('dummy_file.txt')}")
    solution = all_longest("./")
    for key, value in solution.items():
        print(f"{key:20s}\t{value}")
    print("-"*20)
