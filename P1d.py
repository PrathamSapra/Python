def reverse_value(user_value):
    if isinstance(user_value, str):
        return user_value[::-1]
    elif isinstance(user_value,list):
        return list(reversed(user_value))
    else:
        return user_value

user_string = input("Enter String to reverse: ")
reversed_string = reverse_value(user_string)
print("Reversed String:", reversed_string)


