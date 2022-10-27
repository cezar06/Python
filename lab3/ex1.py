def ex1(a,b):
    return [set(a).intersection(set(b)), set(a).union(set(b)), set(a).difference(set(b)), set(b).difference(set(a))]

print(ex1([1,2,3,4,5],[1,2,3,4,5,6,7,8,9]))