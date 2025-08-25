def add(a,b):
    return (a+b)
def sub(a,b):
    return (a-b)
def multiplication(a,b):
    return (a*b)
def division(a,b):
    if (b==0):
        return ("Error divide by 0")
    return (a/b)
def modulus(a,b):
    return (a%b)
def squar(a,b):
    return (a**b)

def calculator():
    while True:
        print ("==Calculator==")
        print ("1. Addition")
        print ("2. Subtractor")
        print ("3. Multiplication")
        print ("4. Division")
        print ("5. Modulus")
        print ("6. Squar")
        print ("7. Exit from Calculator")

        choice = input("Enter your choice:1to7: ")

        if choice == "7":
            print ("Calculator exit, Good Bye!")
            break
        if choice in ["1","2","3","4","5","6"]:
            try:
                num1 = float(input("Enter First Number: "))
                num2 = float(input("Enter Second Number: "))
            except:
                print("Invalid Value, Recheck your Value")
                continue

            if choice == "1":
                print(f"Result: {add(num1, num2)}")  
            elif choice == "2":
                print(f"Result: {sub(num1, num2)}")  
            elif choice == "3":
                print(f"Result: {multiplication(num1, num2)}")  
            elif choice == "4":
                print(f"Result: {division(num1, num2)}")  
            elif choice == "5":
                print(f"Result: {modulus(num1, num2)}")  
            elif choice == "6":
                print(f"Result: {squar(num1, num2)}")  
        else:
            print("Invalid choice, please select from 1 to 7.")
    
calculator()
    


