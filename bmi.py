print("Welcome to BMI Calculator:\n")
weight = float(input("Enter your weight in kg: "))
print("Your Weight is: " + str(weight) + " kg\n")
height = float(input("Enter your height in meters: "))
print("Your height is: " + str(height) + " meters\n")
BMI = float(weight / (height ** 2))
print("Your BMI(BODY MASS INDEX) is: " + str(round(BMI, 2)))
print("And,")
if BMI < 18.5:
    print("you are Under Weight...!!")
elif BMI < 25:
    print("you have a Normal Weight...!!")
elif BMI < 30:
    print("you are Over Weight...!!")
elif BMI < 35:
    print("you are Obese...!!")
else:
    print("you are Clinically Obese...!!")