'''
Exercise 6: English -> Pig Latin translator
now on a sentence.
'''

def en_to_pg (word):
    '''
    Convert a single string into a string in Piglatin
    '''
    # First of all, check if the word end with punctualization
    result = ''
    if word[-1] in '.,:"!?-':
        result = word[-1]
        word = word[:-1]

    # old rule on the basic exercise
    #    if word[0].lower() in 'aeiou':
    # New rule: manupulate if the word contains exacly 2 vowels:
    if len(set(word).intersection(set('aeiou'))) == 2:
        result = word + 'way' + result
    else:
        result = word[1:] + word[0] + 'ay' + result

    return result
#---

if __name__ == '__main__':
    user_input = ' '
    while len(user_input) > 0:
        user_input = input("Translate: ")

        if len(user_input) > 0:
#            sentence = user_input.split(" ")
            sentence = user_input.split()

            for word in sentence:
                if len(word) > 0:
                    print(en_to_pg(word))
