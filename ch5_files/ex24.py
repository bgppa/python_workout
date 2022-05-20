'''
Exercise 24: creating a file which is a reversed copy of another.
'''

def reverse_file(filename_in, filename_ou):
    '''
    Create an output file which reverses every line of the file in input.
    '''
    counter = 0
    try:
        with open(filename_in, 'r') as file_in:
            with open(filename_ou, 'w') as file_ou:
                for line in file_in:
                    if line:
                        tmp = line.rstrip()[-1::-1]
                        tmp += '\n'
                        file_ou.write(tmp)
                        counter += 1
    except FileNotFoundError:
        print(f"ERROR: file {filename_in} not found")

    print(f"{counter} lines written")
    return counter
#---


if __name__ == '__main__':
    reverse_file("dummy_file.txt", "some_output.txt")
    reverse_file("some_output.txt", "equal_to_dummy.txt")
