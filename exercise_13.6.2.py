'''
Instructions
Use recursion to write a function is_sorted that consumes a list of numbers and produces True if the items in the list appear in sorted order and False otherwise. 
A list of length zero or one is always in sorted order.

Hints:
Make sure that you have a base case.
Make sure to use the function on a shorter list.
Before calling the function, first check to see if the list is of length zero or one or if the first number is larger than the second number.
'''
def is_sorted(numbers):
    if len(numbers)<2:
        return True
    elif numbers[0]> numbers[1]:
        return False        
    else:
        return is_sorted(numbers[1:])
