a1 = int(input("Enter the number in Bengali: "))
a2 = int(input("Enter the number in English: "))
a3 = int(input("Enter the number in Maths: "))

# Check subject-wise pass
if (a1 < 25 or a2 < 25 or a3 < 25):
    print("You have failed (one or more subjects have less than 25 marks)")
else:
    total_percentage = (100 * (a1 + a2 + a3)) / 300
    print(total_percentage, "% Total percentage")

    if (total_percentage > 90):
        print("You passed with Distinction")
    elif (total_percentage > 75):
        print("You passed with First Class")
    elif (total_percentage > 45):
        print("You passed with Second Class")
    elif( total_percentage > 35):
        print("You passed with Third Class")
    else:
        print("You have failed (overall percentage too low)")
