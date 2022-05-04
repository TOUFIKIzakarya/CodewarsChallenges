def array_diff(a, b):
    L =[]
    if b == []:
        return a
    if a == []:
        return []
    for elt in a: 
        if elt not in b :
            L.append(elt)
    return L