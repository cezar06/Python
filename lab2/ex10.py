def ex10(*lists):
    list_of_tuples = []
    for i in range(len(lists[0])):
        list_of_tuples.append(tuple([item[i] for item in lists]))
    return list_of_tuples

print(ex10([1,2,3], [5,6,7], ["a","b","c"]))