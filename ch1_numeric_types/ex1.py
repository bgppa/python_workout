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
    lifes = 10
    while guess != num and lifes > 0:
        guess = int(input(f"Enter an integer [{lifes} tries]: "))
        if guess == num:
            print("*Guessed*")
        else:
            lifes -= 1
            if guess > num:
                print("Too high!")
            else:
                print("Too low!")
    return num
#--


if __name__ == '__main__':
    solution = guessing_game()
    print(f"[the number was {solution}]")
