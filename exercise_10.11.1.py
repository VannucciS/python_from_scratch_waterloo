'''
Two numbers are relatively prime if there is no number, other than 1, of which they are both multiples.

Use a for loop to write a function rel_prime that consumes two positive integers and determines if they are relatively prime, producing True if they are and False otherwise.

You might wish to use is_multiple as a helper function.
'''
def is_multiple(number, factor):
    return number % factor == 0

def rel_prime(one,two):
    number_one = []
    number_two = []
    if type(1)!= type(one) and type(1) != type(two):
        return false
    for i in range(2,one+1):
        if is_multiple(one,i):
            number_one.append(i)
    for j in range(2,two+1):
        if is_multiple(two,j):
            number_two.append(j)
    print(number_one, number_two)
    for i in range(len(number_one)):
        for j in range(len(number_two)):
            if number_one[i]
        
                   
        return True

print(rel_prime(5,25))
