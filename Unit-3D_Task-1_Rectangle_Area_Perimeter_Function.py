#Rectangle_Area_Perimeter_Function
l=float(input("ENTER A LENGTH : "))
b=float(input("ENTER THE BREATH : "))
def rec(l,b):
    area=l*b
    perimeter=2*(l+b)
    return area , perimeter
result_area, result_perimeter=rec(l,b)
print("THE AREA OF RECTANGLE : ",result_area )
print("THE PERIMETER OF RECTANGLE : ",result_perimeter)