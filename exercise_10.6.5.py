'''
Instructions
A Canadian postal code is of the form "A9A 9A9", where 9 represents a digit and A represents an upper-case letter.

Fill in the helper functions and the main function, using for loops in the helper functions.

Do not allow lower-case letters.

Hints:
Use isspace to determine if a character is a space.
Consider using tests to make sure that your helper functions work correctly.
You might try using print statements to check intermediate values.
Feedback on your program:
Make sure your function works when the input is has a digit in the second-to-last place.
Make sure your function works when the input has a lower-case letter.
'''
def all_upper(entry):
    """Determines if a string is all upper-case letters

       Preconditions:
       entry: string

       Parameter:
       entry: candidate string to check

       Returns: True if so, False otherwise
    """
    #return entry.isupper()
    #return any(i.islower() for i in entry) - didnt work
    
    for i in entry:
        if i.islower():
            return False
    return True
            
        
def all_digit(entry):
    """Determines if a string is all digits

       Preconditions:
       entry: string

       Parameter:
       entry: candidate string to check

       Returns: True if so, False otherwise
    """
    for i in entry:
        if i.isalpha():
            return False
    return True


def postal_code(entry):
    """Determines if a string is A9A 9A9 in form.

       Preconditions:
       entry: string

       Parameter:
       entry: candidate string to check

       Returns: True if so, False otherwise
    """    
    ## Check length
    if len(entry)!=len('A9A 9A9'):        
        return False
    ## Form a string caps of the "A" entries
    word = entry[0] + entry[2] + entry[5]
    print(word)
    ## Form a string nums of the "9" entries
    nums = entry[1] + entry[4] +entry[6]    
    ## Check for the middle blank
    if not entry[3].isspace():        
        return False
    ## Check that nums is all digits
    for n in nums:
        return all_digit(n) 
    print(n)
    ## Check that caps is all upper-case
    return all_upper(word) 
