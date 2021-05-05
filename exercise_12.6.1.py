'''
Instructions
Write a function number_pixels that consumes a list of lists of strings (representing an image) and a string colour. 
Your function should produce the number of entries that match colour.

Hints:
Use a loop to process each list in the input.
Use a second loop to process each string in a list.
'''
def number_pixels(lst, colour):
    count = {}
    for i in lst:
        for e in i:
            if e in count:
                count[e] = count[e]+1
            else:
                count[e] = 1
    most = 0
    best = 'empty'
    for c, n in count.items():
        if c == colour:
            if n>most:
                most = n
                best = c
    return most
