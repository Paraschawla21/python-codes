print("\nWelcome to love calculator...!!\n")
name1 = input("Enter your Name: ")
name2 = input("Enter their Name: ")
final_name = name1.lower() + name2.lower()
print(f"\nYour combined name is {final_name}\n")
t = final_name.count("t")
r = final_name.count("r")
u = final_name.count("u")
e = final_name.count("e")
true = t + r + u + e
l = final_name.count("l")
o = final_name.count("o")
v = final_name.count("v")
e = final_name.count("e")
love = l + o + v + e
love_score = int(str(true) + str(love))
print(f"\nYour Love Score = {love_score}\n")
if (love_score < 10) or (love_score > 90):
    print(f"Your score is {love_score}, you go together like coke and mentos...!!")
elif (love_score >= 40) and (love_score <= 55):
    print(f"Your score is {love_score}, you are alright together...!!")
else:
    print(f"Your score is {love_score}...!!")