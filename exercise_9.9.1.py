'''
Write a function sum that consumes a list of numbers and produces the total of all the numbers in the list.
'''
def sum(ls):
    counter = 0
    total = 0
    while counter < len(ls):
        total = total + ls[counter]
        counter+=1
    return total
