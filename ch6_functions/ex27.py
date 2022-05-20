'''
Excercise 27: Password Generator.
'''
import random

def create_password_generator(valid_chars):
    '''
    Given a list of characters return a password-generator function,
    locally named _gen_, that produce strings using only them.
    Check _gen_ below for more information.
    '''
    def gen(length):
        '''
        Return a random string on length _length_.
        it contains only characters from _valid_chars_
        '''
        word = []
        for _ in range(length):
            word.append(random.choice(valid_chars))
        return ''.join(word)
    #---
    return gen
#---


def checker(candidate, min_upper=1, min_lower=1, min_punct=1, min_digits=1):
    '''
    Count lower cases, upper cases, punctuation and digits in the
    string _candidate_. Check if their quantity is higher that the minimums.
    '''
    stats = {'upper':0, 'lower':0, 'punct':0, 'digits':0}
    invalid_chars = False

    for letter in candidate:
        if letter.isupper():
            stats['upper'] += 1
        elif letter.islower():
            stats['lower'] += 1
        elif letter.isdigit():
            stats['digits'] += 1
        elif letter in ";:-!+":
            stats['punct'] += 1
        else:
            print(f"Letter {letter}: not allowed")
            invalid_chars = True
            break

    print(stats)
    if stats['upper'] >= min_upper and stats['lower'] >= min_lower:
        if stats['punct'] >= min_punct and stats['digits'] >= min_digits:
            if not invalid_chars:
                return True
    return False
#---


if __name__ == '__main__':
    generator_one = create_password_generator("asdfghjkl!ABRGJ012343K")
    for ith in range(1,10):
        psswd = generator_one(ith)
        print(f"Password: {psswd}")
        print(checker(psswd))
