def ex7(*args):
    result = {}
    for i in range(len(args)):
        for j in range(i+1, len(args)):
            result[str(args[i]) + " | " + str(args[j])] = args[i] | args[j]
            result[str(args[i]) + " & " + str(args[j])] = args[i] & args[j]
            result[str(args[i]) + " - " + str(args[j])] = args[i] - args[j]
            result[str(args[j]) + " - " + str(args[i])] = args[j] - args[i]
    return result

print(ex7({1,2}, {2, 3}))
print(ex7({1,2}, {2, 3}, {3, 4}))