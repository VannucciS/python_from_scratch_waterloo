'''
Use a for loop to write a function has_digit that consumes a nonempty string and determines whether or not there is at least one digit in the string, 
producing True if so and False otherwise.

Hints:
Use isdigit to check if a character is a digit.
You can use for char in word to loop through each character in the string word.
Using return in the body of the loop will result in an early exit from the loop.
'''
def has_digit(string):
    count=0
    for i in string:
        print(i)
        if i.isdigit():
            count+=1
    if count>0:
        return True
    else:
        return False
