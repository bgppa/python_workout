'''
Using the main object programmin-oriented functionalities
in a simple zoo context.
'''

class Animal():
    '''
    Representing an animal with various characteristics.
    '''
    def __init__(self, specie = "no_set", color = "no_set", legs = "no_set"):
        self.specie = specie
        self.color = color
        self.legs = legs

    def __repr__(self):
        return f"A {self.color} {self.specie} with {self.legs} legs"
#---

class Wolf(Animal):
    '''
    an Animal with 4 legs, belonging to the specie _wolf_
    '''
    def __init__(self, color = "no_set"):
        Animal.__init__(self, "wolf", color, 4)
#---

class Sheep(Animal):
    '''
    an Animal with 4 legs, belonging to the specie _sheep_
    '''
    def __init__(self, color = "no_set"):
        Animal.__init__(self, "sheep", color, 4)
#---

class Snake(Animal):
    '''
    an Animal with 0 legs, belonging to the specie _snake_
    '''
    def __init__(self, color = "no_set"):
        Animal.__init__(self, "snake", color, 0)
#---

class Parrot(Animal):
    '''
    an Animal with 2 legs, belonging to the specie _parrot_
    '''
    def __init__(self, color = "no_set"):
        Animal.__init__(self, "parrot", color, 2)
#---

class Cage():
    '''
    Contains a limited amount of animals.
    '''
    def __init__(self, max_animals = 1):
        self.max_animals = max_animals
        self.contained = []


    def add_animal(self, animal):
        '''
        Add a single animal to the cage.
        '''
        if len(self.contained) < self.max_animals:
            self.contained.append(animal)
        else:
            print(f"Cage with max {self.max_animals} if full")
            print(f"Containing: {self.contained}")

    def __repr__(self):
        res = f"Cage with capacity of {self.max_animals} animals. Content:\n"
        tmp = ", ".join(str(animal) for animal in self.contained)
        return res + tmp
#---

class Zoo():
    '''
    Ordered collection of cages.
    '''
    def __init__(self):
        '''
        Starting zoo has no cages.
        '''
        self.total_cages = []


    def add_cage(self, *allcages):
        '''
        Add an arbitrary number of cages
        '''
        for a_cage in allcages:
            self.total_cages.append(a_cage)

    def animals_by_color(self, target):
        '''
        Print all the animals having a target color.
        '''
        print(f"Animals of color {target}:")
        for nth_cage in self.total_cages:
            for nth_animal in nth_cage.contained:
                if nth_animal.color == target:
                    print(nth_animal)

    def animals_by_legs(self, target):
        '''
        Print all the animals having a target number of legs.
        '''
        print(f"Animals with {target} legs:")
        for nth_cage in self.total_cages:
            for nth_animal in nth_cage.contained:
                if nth_animal.legs == target:
                    print(nth_animal)

    def number_of_legs(self):
        '''
        Calculate the total number of legs
        '''
        tot = 0
        for nth_cage in self.total_cages:
            for nth_animal in nth_cage.contained:
                tot += nth_animal.legs
        print(f"Total number of legs: {tot}")

    def __repr__(self):
        res = f"This Zoo contains {len(self.total_cages)} cages:\n"
        for a_cage in self.total_cages:
            res = res + str(a_cage) + '\n\n'
        return res
#---


if __name__ == '__main__':
    generic = Animal()
    sheep1 = Sheep("white")
    wolf1 = Wolf()
    part1 = Parrot("blue")
    snake1 = Snake("solid")

    print(generic)
    print(sheep1)
    print(wolf1)
    print(part1)

    cage1 = Cage(2)
    cage1.add_animal(wolf1)
    cage1.add_animal(snake1)
    cage1.add_animal(sheep1)
    print(cage1)
    print(snake1)

    cage2 = Cage(10)
    print(cage2)
    cage2.add_animal(part1)
    cage2.add_animal(sheep1)

    myzoo = Zoo()
    myzoo.add_cage(cage1, cage2)
    print(myzoo)
