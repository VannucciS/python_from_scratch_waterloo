'''
Use a for loop to write a function swap_case that consumes a string and produces a string which has the same characters as the input but with any lower-case letter replaced 
by the corresponding upper-case letter and any upper-case letter replaced by the corresponding lower-case letter.
'''

def swap_case(word):
    s=[]
    for i in word:
        if i.islower():
            s.append(i.upper())
        else:
            s.append(i.lower())
    return ''.join(s)
    
    

print(swap_case('aBcDeF'))
