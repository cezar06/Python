def is_palindrome(number):
    if number == number[::-1]:
        return True
    else:
        return False