n = int(input("Enter the number:"))
for i in range(2, n):
    if (n % i) == 0:
        print("The number is not Prime")
        break
else:
    print("The number is prime")