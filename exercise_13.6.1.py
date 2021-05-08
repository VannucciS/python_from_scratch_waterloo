'''
Instructions
Use recursion to write a function has_digit that consumes a string and produces True if the string contains a digit (0 through 9) and False otherwise.

Hints:
Make sure that you have a base case.
Make sure to use the function on a shorter string.
Before calling the function, first check to see if the string is empty or if the first character is a digit.
'''
def has_digit(word):
    if len(word) == 0:
        return False    
    elif word[0].isdigit():
        return True
    else:
        return has_digit(word[1:])
