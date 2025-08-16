a1= int(input("Enter the number1:"))
a2= int(input("Enter the number2:"))
a3= int(input("Enter the number3:"))
a4= int(input("Enter the number4:"))

if (a1 > a2) and (a1 > a3) and (a1 > a4):
    print("Number one is largest")
if (a2 > a1) and (a2 > a3) and (a2 > a4):
    print("Number two is largest")
if (a3 > a2) and (a3 > a1) and (a3 > a4):
    print("Number three is largest")
if (a4 > a2) and (a4 > a3) and (a4 > a1):
    print("Number four is largest")

else: 
    print("All number are equal")
