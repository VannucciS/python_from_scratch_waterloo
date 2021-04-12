'''
Instructions
Using the provided class definition and methods, create a new method aligned such that for objects circ_1 and circ_2, circ_1.aligned(circ_2) is True 
if circ_1 and circ_2 share the same x and y coordinates and False otherwise.

Hints:
Make sure to define the method inside the class definition.
Remember that the object itself is the first parameter for every method.
'''

class Circle:
    """Circle radius, x and y coordinates, colour

       Public methods:
       __init__: initializes a new object
    
       Attributes:
       radius: int or float >= 0; circle radius
       x: int >= 0; x-coordinate of centre
       y: int >= 0; y-coordinate of centre
       colour: string; colour of the circle
    """

    def __init__(self, radius, x, y, colour):
        """Creates new circle
        """

        self.radius = radius
        self.x = x
        self.y = y
        self.colour = colour

    def __str__(self):
        """Prints object
        """

        return self.colour + " circle of radius " + \
            str(self.radius) + " centred at (" + \
            str(self.x) + "," + str(self.y) + ")"

    def area(self):
        """Determines area.
        """
        return math.pi * self.radius ** 2

    def aligned(self, other):
        if self.x == other.x and self.y == other.y:
            return True
        else:
            return False

circ_1 = Circle(10, 10, 10, 'brown')
circ_2 = Circle(20,10,9,'yellow')

print(circ_1.aligned(circ_2))
