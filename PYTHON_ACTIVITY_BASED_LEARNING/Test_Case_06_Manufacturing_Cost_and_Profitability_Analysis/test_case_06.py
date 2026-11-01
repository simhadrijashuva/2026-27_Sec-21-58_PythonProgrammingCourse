# Case Study 6: Manufacturing Cost and Profitability
material = float(input("Enter material cost: "))
labour = float(input("Enter labour cost: "))
machine = float(input("Enter machine cost: "))
wastage = float(input("Enter wastage cost: "))
selling_price = float(input("Enter selling price per item: "))
quantity = int(input("Enter quantity sold: "))

if (material < 0 or labour < 0 or machine < 0 or wastage < 0
        or selling_price < 0 or quantity < 0):
    print("Invalid input!")
else:
    total_cost = material + labour + machine + wastage
    revenue = selling_price * quantity
    profit = revenue - total_cost

    print("Total production cost: Rs.", total_cost)
    print("Sales revenue: Rs.", revenue)

    if profit > 0:
        print("Profit: Rs.", profit)
    elif profit < 0:
        print("Loss: Rs.", -profit)
    else:
        print("No profit, no loss.")

    if total_cost > 0:
        profit_percent = profit / total_cost * 100
        print("Profit percentage:", round(profit_percent, 2), "%")
        if profit_percent >= 20:
            print("Target profit achieved.")
        else:
            print("Target profit not achieved.")
    else:
        print("Profit percentage cannot be calculated.")
