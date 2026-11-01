# Case Study 3: Hospital Billing
name = input("Enter patient name: ")
age = int(input("Enter patient age: "))
consultation = float(input("Enter consultation charge: "))
diagnostic = float(input("Enter diagnostic charge: "))
treatment = float(input("Enter treatment charge: "))

if age < 0 or consultation < 0 or diagnostic < 0 or treatment < 0:
    print("Invalid input!")
else:
    bill = consultation + diagnostic + treatment

    if age >= 60:
        concession = bill * 10 / 100
        bill = bill - concession
        print("Senior citizen concession: Rs.", concession)

    if bill >= 5000:
        category = "HIGH"
    else:
        category = "NORMAL"

    print("Patient:", name)
    print("Final bill: Rs.", round(bill, 2))
    print("Bill category:", category)
