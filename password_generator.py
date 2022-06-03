# Py Password Generator
print("\nWelcome to Py Password Generator...!!\n")
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '-', '+']

no_of_letters = int(input("Enter the number of letters you wish in your password?\n"))
no_of_numbers = int(input("Enter the number of numbers you wish in your password?\n"))
no_of_symbols = int(input("Enter the number of symbols you wish in your password?\n"))

#EASY LEVEL

import random
normal_password = ""
for letter in range(1, no_of_letters + 1):
    normal_password += (random.choice(letters))
for number in range(1, no_of_numbers + 1):
    normal_password += (random.choice(numbers))
for symbol in range(1, no_of_symbols + 1):
    normal_password += (random.choice(symbols))
print(f"\nYour normal_password can be: {normal_password}")

#HARD LEVEL

password_list = []
for letter in range(1, no_of_letters + 1):
    password_list.append(random.choice(letters))
for number in range(1, no_of_numbers + 1):
    password_list.append(random.choice(numbers))
for symbol in range(1, no_of_symbols + 1):
    password_list.append(random.choice(symbols))
print(f"\nYour Password list is: {password_list}")
random.shuffle(password_list)
print(f"Your Password list after shuffling becomes: {password_list}")
tough_password = ""
for char in password_list:
    tough_password += char
print(f"\nYour tough_password can be: {tough_password}\n")