def most_common_letter(string):
    string = string.lower()
    letter = ""
    count = 0
    for i in string:
        if i.isalpha():
            if string.count(i) > count:
                letter = i
                count = string.count(i)
    return letter

def main():
    string = input("Enter a string: ")
    print("The most common letter in the string is: ", most_common_letter(string))

if __name__ == "__main__":
    main()