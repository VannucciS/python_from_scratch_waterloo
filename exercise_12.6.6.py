'''
Instructions
Write a function shuffle that produces the perfect shuffle of two equal-length lists. That is, for one = [1, 3, 5] and two = [2, 4, 6], 
the function should produce [1, 2, 3, 4, 5, 6].

Hint:
Use zip.
'''

def shuffle(list1, list2):
    oneTwo = list()
    if len(list1) == len(list2):
        for i, j in zip(list1, list2):
            oneTwo.append(i)
            oneTwo.append(j)
        return oneTwo
    else:
        return False
