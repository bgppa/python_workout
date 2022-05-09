'''
Measuring the average of user input
'''


def f_average(val_list):
    '''
    Compute the average value in a list of floats, assumed valid.
    '''
    res = 0.
    for i in val_list:
        res += i
    return res / len(val_list)
#---


if __name__ == '__main__':
    user_input = 'No'
    all_values = []

    while len(user_input) > 0:
        user_input = input("Insert value: [ENTER to end] ")
        try:
            all_values.append(float(user_input))
        except ValueError:
            if len(user_input) > 0:
                print(f"{user_input} not a number, ignoring...")

    print(f"Average: {f_average(all_values):.2f}")
