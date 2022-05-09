"""
Number guessing game
"""
import numpy as np

def guessing_game():
    """
    Game where the user should guess a hidden number.
    """
    num = np.random.randint(100)
    guess = -1
    lifes = 5
    while guess != num and lifes > 0:
        raw_guess = input(f"Enter an integer [{lifes} tries]: ")
        # Verify input correctness
        try:
            guess = int(raw_guess)
        except ValueError:
            print("Please insert just an integer")
        else:
            if guess > num:
                lifes -= 1
                print("Too high!")
            elif guess < num:
                lifes -= 1
                print("Too low!")

    # only two causes for exiting loop: guess==num, or lifes <= 0
    if guess == num:
        print("You WIN!")
    else:
        print("You LOSE")

    return num
#--


if __name__ == '__main__':
    solution = guessing_game()
    print(f"[the number was {solution}]")
