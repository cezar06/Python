#3. Compare two dictionaries without using the operator "==" returning True or False. (Attention, dictionaries must be recursively covered because they can contain other containers, such as dictionaries, lists, sets, etc.)

def compareDicts(dict1, dict2):
    if dict1.keys() != dict2.keys():
        return False
    for key in dict1.keys():
        if type(dict1[key]) is dict:
            if not compareDicts(dict1[key], dict2[key]):
                return False
        elif type(dict1[key]) is list:
            if not compareLists(dict1[key], dict2[key]):
                return False
        elif type(dict1[key]) is set:
            if not compareSets(dict1[key], dict2[key]):
                return False
        else:
            if dict1[key] != dict2[key]:
                return False
    return True

def compareLists(list1, list2):
    if len(list1) != len(list2):
        return False
    for i in range(len(list1)):
        if type(list1[i]) is dict:
            if not compareDicts(list1[i], list2[i]):
                return False
        elif type(list1[i]) is list:
            if not compareLists(list1[i], list2[i]):
                return False
        elif type(list1[i]) is set:
            if not compareSets(list1[i], list2[i]):
                return False
        else:
            if list1[i] != list2[i]:
                return False
    return True

def compareSets(set1, set2):
    print (set1, set2)
    if len(set1) != len(set2):
        return False
    for i in set1:
        if type(i) is dict:
            if not compareDicts(i, set2):
                return False
        elif type(i) is list:
            if not compareLists(i, set2):
                return False
        elif type(i) is set:
            if not compareSets(i, set2):
                return False
        else:
            if i not in set2:
                return False
    return True

print(compareDicts({1:2, 3:4, 5:6}, {1:2, 3:4, 5:6}))
print(compareDicts({1:2, 3:4, 5:6}, {1:2, 3:4, 5:7}))
print(compareDicts({1:[2,3,4], 3:4, 5:6}, {1:[2,3,4], 3:4, 5:6}))
print(compareDicts({1:[2,3,4], 3:4, 5:6}, {1:[2,3,5], 3:4, 5:6}))