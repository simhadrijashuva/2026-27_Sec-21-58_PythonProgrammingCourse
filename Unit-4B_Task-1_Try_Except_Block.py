#Implement a Python program that catches ZeroDivisionError when dividing 10 by 0
n=int(input("Enter a number : "))
print("-"*23)
try:
    divide=n/0
except ZeroDivisionError:
    print("can't divided by zero!")
    print("-"*23)
else:
    print(f"THE RESULT : {divide} ")
    print("-"*23)
finally:
    print("Execution completed!")
    print("-"*23)