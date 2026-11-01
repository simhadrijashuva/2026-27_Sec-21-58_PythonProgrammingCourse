# Case Study 10: Attendance Recovery
attended = int(input("Enter classes attended: "))
total = int(input("Enter total classes conducted: "))

if total <= 0 or attended < 0 or attended > total:
    print("Invalid attendance details!")
else:
    percentage = attended / total * 100
    print("Current attendance:", round(percentage, 2), "%")

    extra = 0
    while percentage < 75:
        attended = attended + 1
        total = total + 1
        extra = extra + 1
        percentage = attended / total * 100

    if extra == 0:
        print("You already meet the attendance requirement.")
    else:
        print("Minimum additional classes to attend:", extra)

    print("Attendance after attending extra classes:",
          round(percentage, 2), "%")
