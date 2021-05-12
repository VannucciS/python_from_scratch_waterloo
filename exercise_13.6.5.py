'''
Instructions
Use recursion to write a function contains that consumes a list seq and a value item. Your function should produce True if item is an element of seq and False otherwise.

Do not use the built-in function in.

Hint:
For the base case, determine whether an empty list can contain item.
'''
def contains(seq,item):
    if len(seq) == 0 or item ==0:
        return False
    elif seq[0] == item:
        return True
    else:
        return contains(seq[1:], item)
