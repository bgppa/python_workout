'''
Exercise on adding elements in a dictionary
'''

def rainfall ():
    '''
    Expand the database until entering ENTER
    '''
    data = {}
    done = False

    while not done:
        city = input("City: ").lower().strip()
        if city:
            if city in data:
                print("--- already registered ---")
            else:
                # add the float value
                try:
                    val = float(input("measured rain: "))
                except ValueError:
                    print(" --- invalid data, ingored --- ")
                else:
                    data[city] = val
        else:
            done = True
            print("--- DATA ---")
            for key, value in data.items():
                print(f"{key:10s}{value:.2f}")

    return data
#---


if __name__ == '__main__':
    rainfall()
