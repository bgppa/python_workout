'''
Using a dictionary in a Restaurant menu
'''

def restaurant ():
    '''
    Take orders from user
    '''

    MENU = {'pizza' : 3.14, 'espresso' : 1.00, 'water' : 0.50}
    print("Available items:")
    for key, value in MENU.items():
        print(f"{key:10s}{value:.2f}")

    done = False
    tot = 0.

    while not done:
        user_i = input("Place your order: ").strip().lower()
        # Remember that an empty string is seen as False in a boolean check
        if user_i:
            if user_i in MENU:
                tot += MENU[user_i]
                print(f"{user_i} ordered for {MENU[user_i]:.2f}. Tot:{tot:.2f}")
            else:
                print(f"{user_i} not available in the menu")
        else:
            done = True
    print(f"Thanks for your order. Pay: {tot:.2f}")
    return tot
#---


if __name__ == '__main__':
    restaurant()
