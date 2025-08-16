def max_of_three(a,b,c):
    if a>=b and a>=c:
        return a
    elif b>=a and b>=c:
        return b
    else:
        return c

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
c = int(input("Enter third number: "))

N = max_of_three(a, b, c)

print("The maximum of", a, ",", b, "and", c, "is", N)