'''
Write a function move_to_front that consumes a list and an item and mutates the list by removing the item from its location in the list and making it the first element.
If the item is not in the list, the list should not change. You can assume that all items in the input are distinct.
'''


def move_to_front(lista, item):
    for i in lista:
        if i == item:
            lista.remove(i)
            lista.insert(0,i)
    return lista
    
print (move_to_front(['a','b','c'], 'c'))
