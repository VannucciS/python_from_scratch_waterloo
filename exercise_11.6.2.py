'''
Instructions
Add to your methods for the class Egg by creating the method is_size, where egg_type.is_size(num) is True if an egg of mass num is of the category egg_type and False otherwise.

Hint:
Remember that the object itself is the first parameter for every method.
Feedback on your program:
Make sure your function works when the egg is of the correct category.
Make sure your function works when the egg is not of the correct category.
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
        
    def is_size(self, num):
        self.egg_type = self.name
        self.num = num
        if self.num > self.high:
            return True
        else:
            return False
            
egg_type = Egg(10, 20, 'big')
print(egg_type.is_size(25))
