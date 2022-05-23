'''
Comprehensions and files
'''

def all_upper():
    '''
    Take this file and print it modified words in output.
    '''
    with open("ex31.py", "r") as myfile:
        # Add an X after each letter
        tmp = "".join(word + 'X'
                        for line in myfile.read()
                        for word in line)
        print(tmp)
    return 0
#---


if __name__ == '__main__':
    all_upper()
