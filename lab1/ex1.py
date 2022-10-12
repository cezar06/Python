import sys
from functools import reduce
def gcd(a,b):
    while b:
        a,b = b,a%b
    return a
def main():
    if len(sys.argv) < 3:
        print("Usage: py ex1.py num1 num2 [num3 ...]")
        sys.exit(1)
    numere = [int(x) for x in sys.argv[1:]]
    print("Cel mai mare divizor al numerelor",numere,"este",reduce(gcd, numere))
if __name__ == "__main__":
    main()