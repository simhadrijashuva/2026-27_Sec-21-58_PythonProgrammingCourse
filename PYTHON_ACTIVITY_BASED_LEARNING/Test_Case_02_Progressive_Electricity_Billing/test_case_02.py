# Case Study 2: Progressive Electricity Billing
units = float(input("Enter units consumed: "))

if units < 0:
    print("Invalid units!")
else:
    if units <= 100:
        energy_charge = units * 2
    elif units <= 200:
        energy_charge = 100 * 2 + (units - 100) * 3
    else:
        energy_charge = 100 * 2 + 100 * 3 + (units - 200) * 5

    total = energy_charge + 50

    if total > 1000:
        total = total + total * 5 / 100
        print("5% surcharge applied.")
    else:
        total = total - total * 2 / 100
        print("2% rebate applied.")

    print("Energy charge: Rs.", energy_charge)
    print("Final bill: Rs.", round(total, 2))
