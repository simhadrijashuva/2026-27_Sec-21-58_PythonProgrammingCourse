# Case Study 8: Campus Event Financial Planning
venue = float(input("Enter venue cost: "))
equipment = float(input("Enter equipment cost: "))
catering = float(input("Enter catering cost: "))
transport = float(input("Enter transport cost: "))
certificates = float(input("Enter certificate cost: "))
sponsorship = float(input("Enter sponsorship amount: "))

if (venue < 0 or equipment < 0 or catering < 0 or transport < 0
        or certificates < 0 or sponsorship < 0):
    print("Invalid input!")
else:
    total = venue + equipment + catering + transport + certificates
    remaining = total - sponsorship
    registration_fee = 200

    print("Total event cost: Rs.", total)
    print("Sponsorship: Rs.", sponsorship)

    if remaining <= 0:
        print("Sponsorship covers all expenses.")
        print("Minimum registrations needed: 0")
    else:
        print("Amount to be collected: Rs.", remaining)
        registrations = int(remaining / registration_fee)
        if remaining % registration_fee != 0:
            registrations = registrations + 1
        print("Minimum registrations needed:", registrations)
