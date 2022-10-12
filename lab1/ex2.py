def count_vowels(string):
    count = 0
    for i in string:
        if i in "aeiouAEIOU":
            count += 1
    return count

def main():
    string = input("Enter a string: ")
    print("The number of vowels in the string is: ", count_vowels(string))

if __name__ == "__main__":
    main()