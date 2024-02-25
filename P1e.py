#Armstrong and Palindrome

def is_armstrong_number(num):
    num_str = str(num)
    order = len(num_str)

    sum_of_power = 0

    for digit in num_str:
        digit = int(digit)
        sum_of_power += digit ** order

    return sum_of_power == num

def is_palindrome(s):
    s = ''.join(char.lower() for char in s if char.isalnum())
    return s == s[::-1]

print(is_armstrong_number(153))
print(is_armstrong_number(154))
print(is_palindrome("123321"))
