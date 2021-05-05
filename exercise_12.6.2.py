'''
Instructions
For the class Meal, write a method contains such that dinner.contains("eggs") produces True if the object dinner contains the string "eggs" in its list 
of allergens and False otherwise.

Hint:
You can use in to determine if an item is in a list.
'''

class Meal:
    """Meal name, cost, and list of allergens

       Public methods:
       __init__: initializes a new object

       Attributes:
       name: non-empty string; meal name
       cost: int >= 0; cost of meal
       allergens: list of strings; allergens
    """
    
    def __init__(self, name, cost, allergens):
        self.name = name
        self.cost = cost
        self.allergens = allergens
        
    def contains(self, food):
        allergens = self.allergens
        if food in allergens:
            return True
        else:
            return False



feijoada = Meal('feijoada',22, 'soy')

print(feijoada.contains('soy'))
