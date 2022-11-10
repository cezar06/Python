import utils
while True:
    x = input("Enter a number: ")
    if x == "q":
        break
    print(utils.process_item(x))