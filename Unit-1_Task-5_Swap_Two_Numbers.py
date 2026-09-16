#Write a python program to swap two numbers without using a third variable
A=int(input("Enter the first number: "))
B=int(input("Enter the second number: "))
A,B=B,A
print(f"the swapped numbers are {A} and {B}")