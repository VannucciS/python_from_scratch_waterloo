'''
Write a function max_diff that consumes a nonempty list of numbers and produces the maximum difference between any two elements in the list. Do not sort the list.
'''
def max_diff(ls):
    return max(ls)-min(ls)

print(max_diff([1]))
