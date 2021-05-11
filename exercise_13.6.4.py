'''
Instructions
Use recursion to write a function divides_all that consumes a list of positive integers seq and a positive integer factor. Your function should produce True if every item in seq is a multiple of factor and False otherwise. The helper function is_multiple has been provided for you.

Hints:
For your base case, consider a list of length zero.
For the base case, your function should produce True.
'''


def is_multiple(number, factor):
    return number % factor == 0
    
def divides_all(seq,factor):
    print(seq, factor)
    if len(seq) == 0:
        return True
    elif not is_multiple(seq[0], factor):
        return False
    else:
        return divides_all(seq[1:], factor)
