def my_function(*args, **kwargs):
    return sum(kwargs.values())

print(my_function(1, 2, c=3, d=4))

f = lambda *args, **kwargs: sum(kwargs.values())
print(f(1, 2, c=3, d=4))