def my_function(a):
    even = []
    odd = []
    for i in a:
        if i % 2 == 0:
            even.append(i)
        else:
            odd.append(i)
    return list(zip(even, odd))

print(my_function([1, 3, 5, 2, 8, 7, 4, 10, 9, 2]))