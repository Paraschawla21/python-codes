import random
n = int(input("Enter the value of n (prime number): "))
g = int(input("Enter the value of g (prime number): "))
x = random.randint(1, 10)
print(f"Random x = {x}")
y = random.randint(1, 10)
print(f"Random y = {y}")
a = g ** x % n
b = g ** y % n
k1 = b ** x % n
k2 = a ** y % n
print(f"Value of Key 1 = {k1}")
print(f"Value of Key 2 = {k2}")
print(f"Hence, Key 1 = Key 2 = Key = {k1}")