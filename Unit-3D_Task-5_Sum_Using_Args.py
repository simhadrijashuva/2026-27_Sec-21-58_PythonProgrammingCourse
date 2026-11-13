#Unit-3D_Task-5_Sum_Using_Args.py
def sum_n(*n):
    total=0
    for i in n:
        total=total+i
    #print(f"The sum : {total}")
    return total
n=int(input("Enter total numbers : "))
b=[]

for i in range(1,n+1):
    a=int(input(f"Enter a number-{i} : "))
    b.append(a)

tup=tuple(b)
print(f"The sum :{sum_n(*tup)}")
#sum_n(*tup)
