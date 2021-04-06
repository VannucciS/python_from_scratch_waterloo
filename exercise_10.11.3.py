'''
Julius Caesar used a simple code to keep his private correspondence private.

Use a for loop to write a function caesar that encodes a string using Caesar's code. The two inputs are the string in upper-case letters and the integer offset; each character is replaced by the character offset positions away in the alphabet.

You may find it useful to use chr and ord as well as the remainder function, which will allow you to ensure that letters at the end of the alphabet are mapped to upper-case letters at the beginning of the alphabet when the offset is positive; letters at the beginning of the alphabet will be mapped to letters at the end of the alphabet when the offset is negative. The Unicode values of "A" through "Z" are 65 through 90.

Hints:
Consider writing a helper function that adjusts a number to be in the range from 65 to 90.
Your helper function should map 64 to 90 and 91 to 65.
Make sure to use chr on a number and ord on a letter.
'''
def caesar(word, number):
    word = word.upper()
    code = 
    for i in word:
