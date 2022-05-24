'''
An additional exercise on classes and counters.
We point out the fundamental difference between a local variable
in a class, shared with ALL instances, and a self.variable.
'''

class Person():
    '''
    This class increases its counter every time a new istance is created.
    '''
    counter = 0

    def __init__(self):
        Person.counter += 1
        # self.counter += 1 WERE a big mistake, since we want to refer
        # to the variable counter common to ALL instances

    def __repr__(self):
        return f"{self.counter} persons."
        # here it's fine: since there is no instance attribute called
        # counter, it searchs for the one inherited by the parent class

    def __del__(self):
        Person.counter -= 1
#---


if __name__ == '__main__':
    prs1 = Person()
    print(prs1)
    prs2 = Person()
    print(prs2)
    for nth in range(10):
        # a new instance is created and the destroyed
        # at each iteration
        print(Person())

    # The counter must be 2 again, since all the previouses are destroyed
    print(prs2)
