#Enter the number from the user and weather the number is odd or even

number = int(input("Enter a number: "))
mod = number % 2
if mod > 0:
    print("It is an Odd Number")
else:
    print("It is an Even Number")
