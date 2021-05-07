'''
Instructions
Write a function bound_chars that consumes a string and a nonnegative integer bound and produces True if the string has at most bound distinct characters and False otherwise. For example, "raccoon" has five distinct characters, namely "r", "a", "c", "o", and "n".

Hints:
Use a dictionary.
In the dictionary, keep track of the number of times a character has been seen.
You can use len to determine the length of a dictionary.
'''

def bound_chars(string, num):
    dif_char = dict()
    for s in string:
        if s in dif_char .keys():
            dif_char[s] = dif_char[s]+1
        else:
            dif_char[s]= 1       
    print(dif_char)
    if len(dif_char.keys())<=num:
        return True
    else:
        return False
