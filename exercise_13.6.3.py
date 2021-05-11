'''
Instructions
Use recursion to write a function all_equal that consumes a list of numbers and produces True if all the items in the list are equal and False otherwise. 
An input of a list of length zero or one will produce True.

Hints:
Make sure that you have a base case.
Make sure to use the function on a shorter list.
Before calling the function, first check to see if the list is of length zero or one or if the first number is different from the second number.
'''
def all_equal(numbers):
    if len(numbers)<2:
        return True
    elif numbers[0]!=numbers[1]:
        return False
    else:
        return all_equal(numbers[1:])
