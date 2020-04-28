from random import randint

class Die():
    """ Class representing a single die """

    def __init__(self, num_sides=6):
        """ Assume that this die is a cube """
        self.num_sides = num_sides

    def roll(self):
        """ Return a value between 1 and the number of sides the die has """
        return randint(1, self.num_sides)
