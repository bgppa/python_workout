'''
Exercise 20: somehow a clone of wc
'''
import sys

def word_count(filename):
    '''
    Count the words in a file.
    '''
    stats = {'chars':0, 'words':0, 'lines':0, 'u_words':0}
    try:
        with open(filename, 'r') as myfile:
            # Set for collecting the words line by line, elimitating duplicates
            tmp_set = set({})
            for line in myfile:
                stats['lines'] += 1
                stats['chars'] += len(line)
                stats['words'] += len(line.strip().split())
                # Add only the new words
                tmp_set |= set(line.strip().split())
            # The size of this set indicated the number of unique words
            stats['u_words'] = len(tmp_set)

    except FileNotFoundError:
        print(f"Error: file {filename} not found.")

    return stats
#---


if __name__ == '__main__':
    if len(sys.argv) == 2:
        print(f"Opening {sys.argv[1]}")
        solution = word_count(sys.argv[1])
    else:
        print("Opening default file dummy_file.txt")
        solution = word_count("dummy_file.txt")

    for key, value in solution.items():
        print(f"{key:10s}\t{value}")
    print("-"*20)
