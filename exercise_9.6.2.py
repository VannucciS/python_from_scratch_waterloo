'''
Write a function replace that consumes a list, an item old, and an item new and mutates the list by replacing old by new.
If the item old is not in the list, the list should not change. You can assume that all items in the input are distinct (that is, none are the same as any others).
'''
def replace(lista,old,new):
    lista = [new if i in old else i for i in lista]
    return lista


print(replace(["a", "b"], 'a','d'))
