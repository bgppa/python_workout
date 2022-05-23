'''
Creating the dictionary for Gamatria.
'''
import string


def gam_dict():
    '''
    Automatically return the dictionary for the Gamatria code.
    '''
    return {item: elm + 1
            for elm, item in enumerate(string.ascii_lowercase)}
#---


def gamatria_for(word):
    '''
    Converts the word into numbers according the gamatria dict
    '''
    code = gam_dict()
#    return ''.join(str(code[letter]) for letter in word)
    return sum(code.get(letter, 0) for letter in word)
#---

if __name__ == '__main__':
    print(gam_dict())
    print(gamatria_for("ciao_"))
    with open("/usr/share/dict/words", "r") as myfile:
        while True:
            to_search = input("Enter word: ")
            if to_search:
                counter = 1
                for dict_word in myfile:
                    if gamatria_for(dict_word.lower())==gamatria_for(to_search):
                        print(dict_word, end='')
                        counter += 1
                    if counter >= 20:
                        myfile.seek(0)
                        break
            else:
                break
    print("--- done ---")
