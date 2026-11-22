#Implement a Python program to count vowels, consonants, digits and spaces in a string
s=input("Enter a string : ")
s=s.lower()
v="aeiuo"
count=0
num=0
space=0
con=0
spe=0
for i in s:
   
    if i in v:
        count+=1
    elif i.isdigit():
        num+=1
    elif i==" ":
        space+=1
    elif i.isalpha():
        con+=1
    else: 

        spe+=1
print(f"There are ---\n {count}-vowels \n {con}-consonats \n {num}-digits \n {space}-spaces \n {spe}-other \n ---are present in string !")

