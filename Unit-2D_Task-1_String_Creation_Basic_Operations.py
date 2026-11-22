#Implement a Python program to demonstrate string creation and basic operations (concatenation, repetition, slicing)
s=str(input("Enter your first name : "))
s1=str(input("Enter your second name : "))
print(f" using concatenation \n your name : {s+" "+s1}")
print(f" using repeatition ",f"\n {s+s1}"*3,)
print(f"Using slicing \n your first three characters : {s1[0:3]}")

