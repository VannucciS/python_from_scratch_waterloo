'''
Write a function no_zero that consumes a list of numbers and produces a new list formed by removing all the zeroes from the input list. Do not mutate the input.
'''

def no_zero(seq):
    i = 0
    ls = []
    while i< len(seq):
        if seq[i] != 0:
            ls.append(seq[i])
        i+=1    
    return ls
