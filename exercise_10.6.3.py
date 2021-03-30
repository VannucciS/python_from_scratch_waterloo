'''
Use a for loop to write a function no_nums that consumes a string and produces a string which has the same characters as the input but with all digits removed.
'''

def no_nums(string):
    s=[]
    for i in string:
        print(i)
        if i.isdigit():
            s.append('')
        else:
            s.append(i)
    return ''.join(s)
    
print(no_nums('a1b2c3d4'))
