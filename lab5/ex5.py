def my_function(a):
    return [i for i in a if type(i) == int or type(i) == float]

print(my_function([1, "2", {"3": "a"}, {4, 5}, 5, 6, 3.0]))