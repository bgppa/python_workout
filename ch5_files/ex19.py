'''
Simple function to convert a file into a dictionary
'''
def passwd_to_dict(filename = 'passwd.txt'):
    '''
    Convert the content of passwd.txt (copied from /etc/passwd)
    into a dictionary username:userid
    '''
    res = {}
    try:
        with open(filename, 'r') as myfile:
            # Create the dictionary
            for line in myfile:
                # if the line is not empty and is not a comment
                if line and line[0] not in "#\n":
                    tmp = line.split(":")
                    res[tmp[0]] = tmp[2]
    except FileNotFoundError:
        print(f"Error: file {filename} not found.")

    return res
#---


if __name__ == '__main__':
    solution = passwd_to_dict()
    for key, value in solution.items():
        print(f"{key:20s}\t{value:20s}")
    print("-"*40)
