def prime_list(num_list):
    prime_list = []
    for num in num_list:
        if is_prime(num):
            prime_list.append(num)
    return prime_list

def is_prime(num):
    if num < 2:
        return False
    for i in range(2,num):
        if num % i == 0:
            return False
    return True

print(prime_list([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]))