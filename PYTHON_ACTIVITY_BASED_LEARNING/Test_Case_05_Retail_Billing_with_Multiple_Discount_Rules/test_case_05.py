# Case Study 5: Retail Billing
count = int(input("Enter number of products: "))
subtotal = 0
valid = True

if count <= 0:
    print("Invalid product count!")
else:
    for i in range(count):
        print("\nProduct", i + 1)
        name = input("Enter product name: ")
        price = float(input("Enter price: "))
        quantity = int(input("Enter quantity: "))

        if price < 0 or quantity <= 0:
            print("Invalid product details!")
            valid = False
            break

        amount = price * quantity
        subtotal = subtotal + amount
        print(name, "amount: Rs.", amount)

    if valid:
        if subtotal >= 2000:
            discount = subtotal * 10 / 100
        else:
            discount = 0

        taxable_amount = subtotal - discount
        tax = taxable_amount * 5 / 100
        final_bill = taxable_amount + tax

        print("\nSubtotal: Rs.", subtotal)
        print("Discount: Rs.", discount)
        print("Tax: Rs.", tax)
        print("Final bill: Rs.", round(final_bill, 2))
