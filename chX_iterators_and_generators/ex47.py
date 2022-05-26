'''
Defining a class that iterates N times in an object.
If N is bigger that the number of elements, repeats from the beginning.
Example: N = 4, object = "abc". Produces: abca
'''

class Circle():
    '''
    Our iterator with the property mentioned above.
    Being an iterator, by defintion it must provide an __iter__ method
    whose purpose is to call a __next__ function.
    It returns elements and check when evoke StopIteration.
    Using an external object with __next__ allows to iterate in the object
    multiple times, basically because the counter is reset at every instance.
    '''
    def __init__(self, sequence, nelm):
        '''
        We want to iterate in the sequence nelm number of times.
        Store these information on the class instance.
        '''
        self.sequence = sequence
        self.nelm = nelm

    def __iter__(self):
        '''
        The iter method indicate where to find the __next__ method.
        In this case, in CircleIterator. Since all the information we need
        is stored in the class self, it will be the only argument.
        '''
        return CircleIterator(self)
#---


class CircleIterator():
    '''
    Assume that the interator object contains the sequence
    and the information about how many times to iterate.
    '''
    def __init__(self, iterator_object):
        '''
        When called, store locally the required information.
        '''
        self.sequence = iterator_object.sequence
        self.ntimes = iterator_object.nelm
        self.counter = 0

    def __next__(self):
        '''
        Determine how to slide along the iterator_object.
        '''
        if self.counter < self.ntimes:
            res = self.sequence[self.counter % len(self.sequence)]
            self.counter += 1
            return res
        raise StopIteration
#---


if __name__ == '__main__':
    d = [1, 2, 3, 4]
    prova = Circle(d, 2)
    print("Iterating 2 times:")
    for i in prova:
        print(i)
    print("Iterating 2 times, again, to check the reset:")
    for i in prova:
        print(i)
    print("Iterating 10 times:")
    prova10 = Circle(d, 10)
    for i in prova10:
        print(i)
