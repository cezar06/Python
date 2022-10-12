def count_bits(number):
    binary = bin(number)
    count = 0
    for i in binary:
        if i == "1":
            count = count + 1
    return count

def main():
    number = int(input("Enter a number: "))
    print("The number of bits with value 1 is: ", count_bits(number))

if __name__ == "__main__":
    main()