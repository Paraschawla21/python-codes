name = input("Give everybody's name separated by a comma: ")
names = name.split(', ')
print(names)
import random
items = len(names)
random_name = random.randint(0, items - 1)
payee = names[random_name]
print(payee + " is going to buy the meal today")
# payee = random.choice(names)
# print(payee + " is going to buy the meal today")