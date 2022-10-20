def ex7(list):
    palindrome_list = []
    for item in list:
        if str(item) == str(item)[::-1]:
            palindrome_list.append(item)
    return (len(palindrome_list), max(palindrome_list))

print(ex7([11122111, 878, 242, 24442]))