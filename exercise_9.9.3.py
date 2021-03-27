"""
Write a function remove_zero that uses mutation to remove all zeroes from an input list of numbers.
"""

def remove_zero(seq):
    i = 0
    while i< len(seq):
        if seq[i] == 0:
            seq.pop(i)
        i+=1    
    return seq
        
print(remove_zero([1,2,0,3,5,4,0,3,5,0]))
