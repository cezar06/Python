def my_function(*args, **kwargs):
    result = 0
    for arg in args:
        if arg in kwargs.values():
            result += 1
    return result

print(my_function(1, 2, 3, 4, x=1, y=2, z=3, w=5))