#Simple_Interest_Default_Args
p=int(input("Enter a Principal Interest : "))
t=int(input("Enter a Time : "))
r=int(input("Enter a Rate of Interest: "))
def simple(p,t,r=5):
    simple=(p*t*r)/100
    return simple
simple2=simple(p,t,r)
print(f"The Simple Interest : {simple2}")
