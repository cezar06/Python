def ex12(list):
    list_of_lists = []
    for item in list:
        list_of_lists.append([word for word in list if word[-2:] == item[-2:]])
    for i in range(len(list_of_lists)):
        for j in range(len(list_of_lists)):
            if i != j and list_of_lists[i] == list_of_lists[j]:
                list_of_lists[j] = []
    list_of_lists = [item for item in list_of_lists if item != []]
    return list_of_lists

print(ex12(["ana", "banana", "carte", "arme", "parte"]))