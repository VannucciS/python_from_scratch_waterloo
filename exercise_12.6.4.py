'''
Instructions
Write a function code that consumes a string and a dictionary such that the keys in the dictionary are strings of length 1 and 
the values in the dictionary are strings. Your function should produce the string formed by replacing each character in the input that matches a key with the corresponding value.
If a character in the input does not match a key, it should be copied unchanged.

Hint:
You can use in to determine if a string is a key in the dictionary.
'''
def code(string, dic):
    output = list()
    for i in string:
        if i in dic.keys():
            output.append(str(dic.get(i)))
        else:
            output.append(i)
    return "".join(output)
