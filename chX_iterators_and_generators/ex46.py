'''
Implementing a clone of _enumerate_
'''

class Myenumerate():
    '''
    Iterating in this class will print indeces and contents,
    precisely as done with enumerate.
    '''
    def __init__(self, sequence):
        try:
            iter(sequence)
        except TypeError:
            print("Object not iterable, nothing to do")
            self.sequence = []
        else:
            self.sequence = sequence

    def __iter__(self):
        # the __next__ method is inside this object, so returning self
        return HelperIterator(self)
#---

class HelperIterator():
    '''
    Iterator objext for Myenumerate
    '''
    def __init__(self, obj_enumerate):
        self.sequence = obj_enumerate.sequence
        self.counter = 0

    def __next__(self):
        if len(self.sequence) > self.counter:
            res = (self.counter, self.sequence[self.counter])
            self.counter += 1
            return res
        raise StopIteration
#---


if __name__ == '__main__':
    seq = "abcd"
    print("Using Python enumerate:")
    for idx, elm in enumerate(seq):
        print(idx, elm)

    print("Using my implementation:")
    for idx, elm in Myenumerate(seq):
        print(idx, elm)

    print("Generating an error on purpose:")
    Myenumerate(4)

    print("Using my implementation, again, checking that it restarts:")
    for idx, elm in Myenumerate(seq):
        print(idx, elm)
