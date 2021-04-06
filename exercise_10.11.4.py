'''
Instructions
Use a for loop to write a function equals that consumes two lists and produces True if each pair of corresponding values is equal and False otherwise.

Hints:
Make sure that your function works when the lengths of the lists are not the same.
The function can return False as soon as a mismatch is found.
'''

def equals(ls1, ls2):
    if ls1 < ls2:
        ls1, ls2 = ls1, ls2
    else:
        ls1, ls2 = ls2, ls1
    if len(ls1) == 0 and len(ls2) == 0:
        return True
    if len(ls1) !=len(ls2):
        return False
    for i in range(len(ls1)):
        if ls1[i] != ls2[i]:
            return False
        else:
            return True


print(equals([1], [1,2]))
