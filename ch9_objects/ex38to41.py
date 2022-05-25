'''
Creating some classes representing ice creams.
It mixed exercises 38, 39, 40 and 41.
Important to point out the difference between
class.nameofvariable, and self.nameofvariable.
'''

class Scoop():
    '''
    Class representing an ice-cream scoop.
    Empty argument because it does not derive from another class.
    '''
    def __init__(self, flavor = 'no_flavor_'):
        # Inizialize the scoop with the chosen flavor
        self.flavor = flavor

    def __repr__(self):
        # Choose how to display the class under print
        return f"Scoop with flavor: {self.flavor}"
#---


class Bowl():
    '''
    Class representing a set of Scoops
    '''
    # By default, all Bowls are limited to 2 scoops
    limit = 3

    def __init__(self):
        # initially, empty
        self.contained_scoops = []

    def add_scoop(self, *newscoops):
        '''
        can give an arbitrary number of scoops
        '''
        for single_scoop in newscoops:
            # if the instance has a different self.limit value, that one
            # will constitute the limit. Otherwise read Bowl.limit
            if len(self.contained_scoops) < self.limit:
                self.contained_scoops.append(single_scoop)
            else:
                print(f"Warning: limit of {self.limit} scoops exceeded!")

    def __repr__(self):
        # Set the visualization
        res = "This Bowl contains:\n"
        for scoop in self.contained_scoops:
            res += f"scoop of {scoop.flavor}\n"
        return res
#---



def create_scoops(flav1, flav2, flav3):
    '''
    Create three scoops with corresponding flavors.
    '''
    return [Scoop(flav1), Scoop(flav2), Scoop(flav3)]
#---


class FixedBowl(Bowl):
    '''
    This is a Bowl with a max hard set to be 2.
    '''
    def __init__(self):
        Bowl.__init__(self)
        self.limit = 2

    # All the rest is the same, therefore I don't need to change nothing else.
#---



if __name__ == '__main__':
    result = create_scoops("vaniglia", "crema", "limone")
    for icecream in result:
        print(icecream)

    bwl = Bowl()
    for nth in result:
        bwl.add_scoop(nth)

    print(bwl)
    bwl.add_scoop(Scoop("amarena"))
    print(bwl)

    print("For the exercise 41")
    exercise_41 = FixedBowl()
    print(exercise_41)
    for nth in result:
        exercise_41.add_scoop(nth)
    print(exercise_41)
