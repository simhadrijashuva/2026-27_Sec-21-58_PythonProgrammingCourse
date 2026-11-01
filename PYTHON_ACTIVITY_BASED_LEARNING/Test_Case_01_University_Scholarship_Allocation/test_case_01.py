# Case Study 1: University Scholarship Allocation
name = input("Enter student name: ")
aggregate = float(input("Enter aggregate percentage: "))
s1 = float(input("Enter subject 1 marks: "))
s2 = float(input("Enter subject 2 marks: "))
s3 = float(input("Enter subject 3 marks: "))
attendance = float(input("Enter attendance percentage: "))
income = float(input("Enter annual family income: "))

if (aggregate >= 75 and s1 >= 60 and s2 >= 60
        and s3 >= 60 and attendance >= 75
        and income <= 250000):
    print(name, "is ELIGIBLE for scholarship.")
else:
    print(name, "is NOT ELIGIBLE for scholarship.")
