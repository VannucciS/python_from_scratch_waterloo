'''
Write a function divides_all that consumes a list of positive integers seq and a positive integer factor. 
Your function should produce True if every item in seq is a multiple of factor and False otherwise. The helper function is_multiple has been provided for you.
'''

def is_multiple(number, factor):
    return number % factor == 0
    
def divides_all(seq, factor):
    counter = 0
    result = []
    while counter < len(seq):
        result.append(is_multiple(seq[counter], factor))
        counter+=1
    try:
        return sum(result)/len(seq) == 1.0
    except ZeroDivisionError:
        return False
