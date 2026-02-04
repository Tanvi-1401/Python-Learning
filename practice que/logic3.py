def hillvalley(l):
    n = len(l)
    if n < 4:
        return False

    i = 1

    if l[1] > l[0]:
        
        while i < n and l[i] > l[i-1]:
            i += 1
        
        if i == 1 or i == n:
            return False
        
        while i < n and l[i] < l[i-1]:
            i += 1
        
        return i == n

    elif l[1] < l[0]:

        while i < n and l[i] < l[i-1]:
            i += 1
        
        if i == 1 or i == n:
            return False
    
        while i < n and l[i] > l[i-1]:
            i += 1
        
        return i == n

    return False
