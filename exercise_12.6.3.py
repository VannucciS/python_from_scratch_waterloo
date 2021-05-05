'''
Instructions
Now create a function (not a method) all_contain that consumes a list of Meal objects and a string allergen. Your function should produce a list of the names of 
all objects in the list that contain the string in their allergen list.

Hints:
Make sure that your function definition is not part of the class definition.
Keep track of what is a list and what is an object.
Feedback on your program:
Make sure your function works when the number of objects containing the string is more than 1.
Make sure your function works when the number of objects containing the string is 1.
Make sure your function works when the number of objects containing the string is 0.
Make sure your function works when the input list is of length 0.
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
            
def all_contain(lst,item):
    allergy = set()
    if len(lst) == 0 or len(item)==0:
        return 'Empty'
    for i in lst:
        for e in item:
            if i == e:
                allergy.add(i)
    return allergy
