def ex6(*lists, x):
    single_list = []
    for list in lists:
        single_list.extend(list)
    print(single_list)
    new_list = []
    for item in single_list:
        if single_list.count(item) == x:
            new_list.append(item)
    return new_list
print(ex6([1, 2, 3], [2, 3, 4], [4, 5, 6], [4, 1, "test"], x=2))