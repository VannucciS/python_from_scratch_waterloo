def is_pal(entry):
    if len(entry) <= 1:
        return True
    else:
        print(len(entry))
        return entry[0] == entry[-1] and is_pal(entry[1:-1])



print(is_pal('aaaaaaaaaaaaaaaaaabaaaaaaaaaaaaaaa'))
        
    
