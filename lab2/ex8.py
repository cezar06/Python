def ex8(listOfStrings, x=1, flag=True):
    listOfLists = []
    for string in listOfStrings:
        listOfLists.append([])
        for char in string:
            if flag:
                if ord(char) % x == 0:
                    listOfLists[-1].append(char)
            else:
                if ord(char) % x != 0:
                    listOfLists[-1].append(char)
    return listOfLists

print(ex8(["test", "hello", "lab002"], 2, False))
