def ex6(list):
    a = len(set(list))
    b = len(list) - a
    return (a,b)

print(ex6([1,2,3,4,5,6,7,8,9,10,1,2,3,4,5,6,7,8,9]))