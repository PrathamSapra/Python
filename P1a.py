#Create a program that asks the user to enter their name and their age. Print out a message addressed to then that tells them the year that they will turn 100 years old.

name = input("Enter name: ")
age = int(input("Enter age:"))
year = str((2023-age)+100)
print(name+ " will be v 100 years old in the year: " +year)
