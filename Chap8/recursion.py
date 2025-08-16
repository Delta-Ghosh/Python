def num(n):
    if (n==0 or n==1):
        return 1
    else:
        return n * num(n-1)
# This code defines a recursive function to calculate the factorial of a number.
n = int(input("Enter a number:"))
num(n)

print("The factorial of", n, "is", num(n)) 
