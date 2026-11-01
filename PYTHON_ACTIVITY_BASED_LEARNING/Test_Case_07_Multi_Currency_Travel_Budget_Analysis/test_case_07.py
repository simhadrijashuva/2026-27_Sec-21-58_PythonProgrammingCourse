# Case Study 7: Multi-Currency Travel Budget
rate = float(input("Enter exchange rate (Rs. per 1 foreign unit): "))
food = float(input("Enter food expense in foreign currency: "))
travel = float(input("Enter travel expense in foreign currency: "))
hotel = float(input("Enter hotel expense in foreign currency: "))
budget = float(input("Enter budget in rupees: "))

if rate < 0 or food < 0 or travel < 0 or hotel < 0 or budget < 0:
    print("Invalid input!")
else:
    food_inr = food * rate
    travel_inr = travel * rate
    hotel_inr = hotel * rate

    total = food_inr + travel_inr + hotel_inr
    fee = total * 2 / 100
    final = total + fee

    print("Food in Rs.:", food_inr)
    print("Travel in Rs.:", travel_inr)
    print("Hotel in Rs.:", hotel_inr)
    print("Conversion fee: Rs.", fee)
    print("Total expense: Rs.", round(final, 2))

    if final <= budget:
        print("Within budget.")
    else:
        print("Budget exceeded by Rs.", round(final - budget, 2))

    if food_inr >= travel_inr and food_inr >= hotel_inr:
        print("Largest expense: Food")
    elif travel_inr >= hotel_inr:
        print("Largest expense: Travel")
    else:
        print("Largest expense: Hotel")
