#smallest of three numbers
a=int(input("Enter first number: "))
b=int(input("Enter second number: "))
c=int(input("Enter third number: "))
if a <= b:
    if a<=c:
        smallest=a
    else:
        smallest=c
else:
    if b<=c:
        smallest=b
    else:
        smallest=c
print(f"The Smallest Number= {smallest} (Among {a},{b},{c}) ")
