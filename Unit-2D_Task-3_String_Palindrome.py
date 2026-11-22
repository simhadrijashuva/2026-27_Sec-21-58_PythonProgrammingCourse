#Implement a Python program to check whether a string is a palindrome
s=input("Enter a String : ")

reverse=s[::-1]
if s==reverse:
    print(f"{s} is polindrome")
else:
    print(f"{s} is not polindrome")
    

