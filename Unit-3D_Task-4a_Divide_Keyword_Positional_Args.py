#Unit-3D_Task-4a_Divide_Keyword_Positional_Args.py
a=int(input("Enter a number-1 : "))
b=int(input("Enter a number-2 : "))
def divide(a,b):
    return (a/b)
#keyword
key=divide(b=a,a=b)
print(f"Divided using keyword argumants : {b}/{a} = {key}")
#position
pos=divide(a,b)
print(f"Divided using position arguments : {a}/{b} = {pos} ")

