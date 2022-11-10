def f9(pairs):
    return [{"sum": i[0] + i[1], "prod": i[0] * i[1], "pow": i[0] ** i[1]} for i in pairs]

print(f9([(5, 2), (19, 1), (30, 6), (2, 2)]))