#Implement a Python program that uses keys, values, items, get, update and pop on a sample dictionary
students={
    "name" : "jashu",
    "course" : "CYBER-SECURITY",
    "age":17
}
students.update({"age":18,"city":"mangalagiri"})
print(f"items: {students.items()}")
print(f"keys : {students.keys()}")
print(f"values : {students.values()}")
print(f"get : {students.get('course')}")
students.update({"age":18,"city":"mangalagiri"})
print(f"update : {students}")
print(f"pop : {students.pop('city')}")
print(f"after pop : {students}")

