'''
Use a for loop to write a function password that produces True if a string is a suitable password and False otherwise. 
The string must contain at least one upper-case letter, at least one lower-case letter, at least one digit, and be of length at least eight.
'''
def password(psw):
    upper, lower, digit = "", "", ''
    if len(psw)<8: # verify if the string has at least length eigth
        return False
    for i in psw:
        if i.isupper() and i.isalpha(): #verify if the string has at least one upper-case letter
            upper = upper +i
        elif i.islower(): # verify if the string has at least one lower-case letter
            lower = lower + i
        elif i.isdigit(): # verify if the string has at least one digit
            digit = digit + i    
    return len(upper) > 0 and len(lower) > 0 and len(digit) > 0
