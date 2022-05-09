'''
Re-implementing a sort of sum function for learning purposes.
The user enter a string, whose elements are stored into a list.
If they are all numbers, are summed, otherwise the sum is done
taking into account single characters and therefore giving back
the original string.
'''


def mysum(*args):
    '''
    Takes a variable number of arguments and return their sum.
    Clearly, the effect will depent on their type.
    '''
    curr_sum = args[0]
    for val in args[1:]:
        curr_sum += val
    return curr_sum
#---


if __name__ == '__main__':

    to_repeat = 'Yes'

    # Repeat if press enter or if starts with Y or y
    while (to_repeat+'y')[0].lower() == 'y':
        to_pass = list(input("Enter the values to sum: "))
        # if ALL the values are numbers, interpret them accordingly
        try:
            numbers_to_pass = []
            for k in to_pass:
                numbers_to_pass.append(float(k))
        except ValueError:
            print("[ --- summing the chars to form a word --- ]")
        else:
            print("[ --- summing numbers --- ]")
            to_pass = numbers_to_pass

        print(f"mysum: {mysum(*to_pass)}")
        to_repeat = input("Repeat? [default = Y] ")
        print(f"[user answer: {(to_repeat+'y')[0].lower()}]")
