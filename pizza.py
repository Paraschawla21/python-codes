print("\nWelcome to Pizza Deliveries!!\n")
pizza = input("Enter the Size of the pizza you want: S, M or L...?? ")
peproni = input("Do you want peproni: Y or N...?? ")
cheese = input("Do you want extra cheese: Y or N...?? ")
bill = 0
if pizza == "S":
    bill += 15
    if peproni == "Y":
        bill += 2
    if cheese == "Y":
        bill += 1
elif pizza == "M":
    bill += 20
    if peproni == "Y":
        bill += 3
    if cheese == "Y":
        bill += 1
else:
    bill += 25
    if peproni == "Y":
        bill += 3
    if cheese == "Y":
        bill += 1

print(f"\nYour Final Pay Amount is: ${bill}\n")