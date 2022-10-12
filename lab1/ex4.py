def convert(string):
    new_string = ""
    for i in range(len(string)):
        if string[i].isupper():
            new_string = new_string + "_" + string[i].lower()
        else:
            new_string = new_string + string[i]
    return new_string

def main():
    string = input("Enter a string: ")
    print("The new string is: ", convert(string))

if __name__ == "__main__":
    main()