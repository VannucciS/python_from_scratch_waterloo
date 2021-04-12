'''
Instructions
Now add a method bigger such that circ_1.bigger(circ_2) is True if circ_1 is bigger than circ_2 and False otherwise.
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
            
    def bigger(self, other):
        if self.radius > other.radius:
            return True
        else:
            return False
