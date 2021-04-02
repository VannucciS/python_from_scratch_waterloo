def palin(word):
    word = word.upper()
    import math
    a = []
    b = []
    mid = math.ceil(len(word)/2)
    if len(word) %2 == 0:
        for i in range (0, mid):
            a.append(word[i])
        for j in range (len(word)-1, mid-1, -1):
            b.append(word[j])
        print(a,b)
        if a == b:
            return True
        else:
            return False
    else:
        for i in range (0, mid-1):
            a.append(word[i])
        for j in range (len(word)-1, mid-1, -1):
            b.append(word[j])
        print(a,b)
        if a == b:            
            return True
        else:
            return False
        
            
                

print(palin('OPedromordepo'))
