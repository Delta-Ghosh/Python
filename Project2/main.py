import random
n = random.randint(1,20)
a= -1
guess = 0

while (a!=n):
    a= int(input("Enter the number between 1 to 20: "))
    guess += 1
    if (a>n):
        print ("Lower number please")
    else :
        print ("Higher number please")
print (f"You have guess the correct number {n} in {guess} attempted.")