'''
Use a for loop to write a function my_power that consumes two inputs base and exponent, where base is a non-negative integer or 
floating point number and exponent is a non-negative integer. Your function should produce base to the exponent power. 
The computation should be made using repeated multiplication.

Hints:
The number of iterations should be equal to exponent.
Use range to iterate.
You should multiply the product so far by base at each iteration of the loop.
The initial value of the product so far should be 1.
'''

def my_power(b, e):
    power=1
    if type(b) != type(1) and b<0 and e<0 and type(e)!=type(1):
        return False
    if (b) == (0) or (e) == (0) or b ==1:
        return power
    else:
        for m in range(e):
            power= power*b
    return power    
            
        

print(my_power(3,1))
