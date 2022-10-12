def count_occurrences(string, substring):
    count = 0
    for i in range(len(string)):
        if string[i:i+len(substring)] == substring:
            count = count + 1
    return count

def main():
    string = input("Enter a string: ")
    substring = input("Enter a substring: ")
    print("The number of occurrences of the substring in the string is: ", count_occurrences(string, substring))
    
if __name__ == "__main__":
    main()