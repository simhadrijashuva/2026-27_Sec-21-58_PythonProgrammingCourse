#Marks_Total_Average_Function
sub1=int(input("ENTER MARKS IN SUBJECT 1 : "))
sub2=int(input("ENTER MARKS IN SUBJECT 2 : "))
sub3=int(input("ENTER MARKS IN SUBJECT 3 : "))
def marks(sub1,sub2,sub3):
    sum=sub1+sub2+sub3
    average=sum//3
    return sum,average
sum,average=marks(sub1,sub2,sub3)
print(f"THE TOTAL MARKS : {sum}")
print(f"THE AVERAGE MARKS : {average}")
