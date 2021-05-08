def sum(seq):
    if len(seq) ==0:
        return 0
    else:
        print(seq)
        return seq[0] + sum(seq[1:])
        
    
    
print(sum([1,0,0,0,0,0,0,0]))
