'''
Simple hex to decimal conversion for user input.
Sure, in real programming, just use 0xFF or int('FF', 16).
'''

def to_decimal_value(char_digit):
    """
    Assuming in input a char representing a single hex digit,
    return its value in base 10.
    """
    for idx, elm in enumerate("0123456789ABCDEF"):
        if char_digit == elm:
            return idx
    return "Not found!"
#--


if __name__ == '__main__':

    converted = 0
    num = input("Enter the number in base 16: ").upper()

    try:
        for digit in num:
            if digit not in "0123456789ABCDEF":
                raise ValueError
    except ValueError:
        print("Not valid, you must insert an integer in base 16.")
    else:
        for idx, elm in enumerate(reversed(num)):
            converted += (16 ** idx) * to_decimal_value(elm)
        print(f"Conversion: {converted}")
