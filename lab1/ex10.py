def count_words(text):
    count = 1
    for i in text:
        if i == " ":
            count  = count + 1
    return count

def main():
    text = input("Enter a text: ")
    print("The number of words in the text is: ", count_words(text))

if __name__ == "__main__":
    main()