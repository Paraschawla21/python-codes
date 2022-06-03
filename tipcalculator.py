print("Welcome to Tip Calculator...!!")
bill = input("What was your total bill...?? $")
a = 10
b = 12
c = 15
tip = input(f"Enter the percentage amount you wish to tip...?? ${a}, ${b} or ${c}...?? $")
persons = input("Enter the number of persons you wish to split the bill for: ")
amount = float((float(bill) + (float(bill) * (int(tip) / 100))) / int(persons))
print("Each person has to pay: $" + str(round(amount, 2)))