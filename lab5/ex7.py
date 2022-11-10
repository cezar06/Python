def process(**kwargs):
    fib = [0, 1]
    for i in range(2, 1000):
        fib.append(fib[i-1] + fib[i-2])
    if "filters" in kwargs:
        fib = [i for i in fib if all([j(i) for j in kwargs["filters"]])]
    if "limit" in kwargs:
        fib = fib[:kwargs["limit"]]
    if "offset" in kwargs:
        fib = fib[kwargs["offset"]:]
    return fib

print(process(limit=10, offset=5, filters=[lambda x: x % 2 == 0, lambda x: x % 3 == 0]))