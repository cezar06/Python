def extract_number(text):
    number = ""
    for i in text:
        if i.isdigit():
            number = number + i
        elif number != "":
            break
    return number

def main():
 
    text = input("Enter a text: ")
    print("The first number extracted from the text is: ", extract_number(text))

if __name__ == "__main__":
    main()