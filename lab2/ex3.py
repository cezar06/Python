def intersect(a,b):
    return list(set(a) & set(b))

def union(a,b):
    return list(set(a) | set(b))

def difference(a,b):
    return list(set(a) - set(b))

def symmetric_difference(a,b):
    return list(set(a) ^ set(b))

def do_all(a,b):
    return (intersect(a,b),union(a,b),difference(a,b),symmetric_difference(a,b))

a = [1,2,3,4,5,6,7,8,9,10]
b = [1,3,5,7,9,11,13,15,17,19]

print(do_all(a,b))