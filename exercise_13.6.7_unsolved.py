'''
Instructions
Use recursion to write a function multisplit that consumes two positive integers total and split and produces the number of times total is repeatedly 
divided into split even pieces before each piece is of size at most 1.

For example, the value returned by multisplit(8, 2) will be 3, since 8 can be split into 2 pieces of size 4, which are then each split into 2 pieces of size 2, 
which are then each split into 2 pieces of size 1 (at which point no further splitting takes place since the pieces are of size at most 1). The value returned by 
multisplit(8, 3) will be 2, since 8 can be split into 3 pieces of size 8/3, which are then each split into 3 pieces of size 8/9 (at which point no further splitting 
takes place since the pieces are of size at most 1).

Hint:
Remember that each call to multisplit returns an integer. Use this number in determining what your function should produce.
'''
def multisplit(total, split):
    count = 0
    if total<=1:
        return count
    else:
        return multisplit(total/split)
    
