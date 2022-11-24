#SAALLZZJJNNNC where:
#S is between 1 and 8
#A is between 00 and 99
#LL is between 00 and 12
#ZZ is between 00 and 31
#JJ is between 01-48, 51 and 52
#NNN is between 000 and 999
#279146358279

import re
def is_valid_number(number):
    return re.search(r'^[1-8][0-9]{2}(0[0-9]|1[0-2])(0[0-9]|[1-2][0-9]|3[0-1])(0[1-9]|1[0-9]|2[0-8]|3[0-8]|4[0-8]|5[0-1]|5[2])([0-9]{3})$', number)
    
def last_digit(number):
    sum = 0
    for i in range(len(number)):
        sum += int(number[i]) * int("279146358279"[i])
    return sum % 11

def is_valid_CNP(number):
    if is_valid_number(number[:-1]):
        if last_digit(number[:-1]) == int(number[-1]):
            return True
    return False
    
print(is_valid_CNP("5011010226754"))