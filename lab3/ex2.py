def ex2(string):
    return {i: string.count(i) for i in string}

print(ex2("Ana has apples."))