'''
Instructions
The Egg class can be used to create categories for eggs. For example, a "Large" egg should have mass in the range from 56 to 62 grams, so that 56 is the lowest mass and 62 is the highest mass possible for this category.

Using the provided class definition and docstring, create methods __init__ and __str__.

Hints:
Make sure to define the method inside the class definition.
Make sure to use self as the first parameter of each method.
Use dot notation to refer to an attribute

'''
class Egg:
    """Egg low and high range of mass
       and category name.
    
       Attributes:
       low: int > 0, lowest mass in grams
       high: int > 0, highest mass in grams
       name: nonempty string, category
    """
    def __init__(self, low, high, name):
        self.low =  low
        self.high =  high
        self.name =  name
