def is_pal(entry):
    mid =  (len(entry)) // 2
    for i in range(mid):
        if entry[i] != entry[-(i+1)]:
            return False
    return True
    
print(is_pal('anna'))
