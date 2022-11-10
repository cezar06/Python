def process_item(x):
    x = int(x)
    for i in range(x+1, 2*x):
        for j in range(2, i):
            if i % j == 0:
                break
        else:
            return i