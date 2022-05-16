'''
Exercise 12: the string that contains the highest number of repeated letters
'''
from collections import Counter

def hr_letter(word):
    '''
    I: a string
    O: the number of highest repeated letter in the string
    '''
    most_freq = 0
    the_letter = ''
    for letter in word:
        tmp_freq = 0
        # Compare to all the letters in the word
        for letter_again in word:
            if letter == letter_again:
                tmp_freq += 1
        # Update the highest frequency if needed
        if tmp_freq > most_freq:
            most_freq = tmp_freq
            the_letter = letter
    return (most_freq, the_letter)
#---


def most_repeating_word(list_of_strings):
    '''
    I: a list of strings
    O: the word that contains the highest number of repeating letters
    '''
    highest_num = 0
    the_word = ''
    the_letter = ''
    for word in list_of_strings:
        tmp = hr_letter(word)
        if tmp[0] > highest_num:
            highest_num = tmp[0]
            the_letter = tmp[1]
            the_word = word
    print(f"most freq is {the_word}, with {highest_num} rep of {the_letter}")
    return the_word
#---

def alternative_sol (list_of_strings):
    '''
    Alternative compact solution by using the Counter object available
    in the _collections_ standard Python3 module
    '''
    return max(list_of_strings,
                        key = lambda wd : Counter(wd).most_common()[0][1])
#---

if __name__ == '__main__':
    lwords = ["ciao", "allora", "aaaah"]
    print(most_repeating_word(lwords))
    print(alternative_sol(lwords))
