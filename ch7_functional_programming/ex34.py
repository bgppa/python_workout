'''
Showing which words into a file are _supervocalic_.
'''

def is_supervocalic(word):
    '''
    Return True is the input contains all vocals.
    '''
#    print(f"checking {word}...")
    for vocal in "aeiou":
        if vocal not in word:
            return False
    return True
#---


def file_supervocalic(filename):
    '''
    Print all the supervocalic words contained in a file.
    '''
    with open(filename, "r") as myfile:
        all_words = ", ".join(word
                                for line in myfile
                                for word in line.strip().split()
                                if is_supervocalic(word))
        print(f"Supervocalic words:\n{all_words}")
    return 1
#---

if __name__ == '__main__':
    file_supervocalic("ex34.py")
