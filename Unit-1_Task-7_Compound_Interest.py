#Write a python program to calculate compound interest
p=float(input("intial principle amount: "))
r=float(input("annual interest rate: "))
n=float(input("number of times interest is compounded: "))
t=float(input("number of years: "))
compound_interest=p * (1 + r / n) ** t
print(f"compound interest is {compound_interest}")