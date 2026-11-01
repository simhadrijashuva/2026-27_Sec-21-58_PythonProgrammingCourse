# Case Study 4: Employee Payroll
name = input("Enter employee name: ")
basic = float(input("Enter basic pay: "))
overtime = float(input("Enter overtime amount: "))
incentive = float(input("Enter incentive amount: "))

if basic < 0 or overtime < 0 or incentive < 0:
    print("Invalid salary details!")
else:
    hra = basic * 20 / 100
    other_allowance = basic * 10 / 100
    gross = basic + hra + other_allowance + overtime + incentive
    deduction = gross * 5 / 100
    net_salary = gross - deduction

    print("\n----- SALARY STATEMENT -----")
    print("Employee:", name)
    print("Basic pay: Rs.", basic)
    print("HRA: Rs.", hra)
    print("Other allowance: Rs.", other_allowance)
    print("Overtime: Rs.", overtime)
    print("Incentive: Rs.", incentive)
    print("Gross salary: Rs.", round(gross, 2))
    print("Deduction: Rs.", round(deduction, 2))
    print("Net salary: Rs.", round(net_salary, 2))
