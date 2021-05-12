'''
Instructions
Use recursion to write a function reverse that consumes a list seq and produces a new list with the same items as seq but in reverse order. 
A list of length zero or one is its own reverse.

Hint:
Make sure to concatenate two lists, not a list and an item.
'''

def reverse(seq):
    ''' como inverter uma lista?
    O primeiro vira o [ultimo, o segundo vira o penultimo e assim por diante...
    '''
    result = list()
    if len(seq)== 0:
        return []
    else:
        return [seq[-1]] + reverse(seq[:-1])
