# # caeser cipher

key = 3
pt = "call me"
ct = ""
for i in pt:
    if i != " ":
        order = ((key + ord(i) - 97) % 26) + 97
        ct += chr(order)
    else:
        ct += " "
print(ct)


# # vernam cipher

k = "xyz".upper()
pt = "pleasecallme".upper()
ct = ""
j = 0
for i in pt:
    j = j % len(k)
    order = (((ord(i) - 65) + (ord(k[j]) - 65)) % 26) + 65
    ct += chr(order)
    j += 1
print(ct)


# hill cipher

from operator import matmul
import numpy as np
t = "CAT".upper()
k = "XYZABCIJK".upper()
tm = []
km = []
for i in t:
    x = ord(i) - 65
    tm.append(x)

temp = []
for j in k:
    y = ord(j) - 65
    temp.append(y)
    if len(temp) == len(t):
        km.append(temp)
        temp = []

l = np.matmul(km, tm)
ct = ""
for k in l:
    ct += (chr((k % 26) + 65))
print(ct)


# play fair cipher

key = input("Enter KEY: ")
key = key.replace(" ", "")
key = key.upper()
my_matrix = [[" " for i in range(5)] for j in range(5)]
result = []
for c in key:
    if c not in result:
        if c != 'J' and c != 'I':
            result.append(c)
        elif c == 'J' and 'I' not in result:
            result.append('I')
for i in range(65, 91):
    if chr(i) not in result:
        if chr(i) == 'I' and 'I' not in result:
            result.append('I')
        elif chr(i) == "J" and 'I' not in result:
            result.append('I')
        elif chr(i) != 'J':
            result.append(chr(i))
k = 0
for i in range(0, 5):
    for j in range(0, 5):
        my_matrix[i][j] = result[k]
        k += 1
        if (my_matrix[i][j] == 'I'):
            print('I/J', end = "  ")
        else:
            print(my_matrix[i][j], end = "   ")
    print()


# rail fence cipher

s = input("Enter string: ")
k = int(input("Enter key: "))
enc = [[" " for i in range(len(s))] for j in range(k)]
flag = 0
row = 0
for i in range(len(s)):
    enc[row][i] = s[i]
    if row == 0:
        flag = 0
    elif row == k-1:
        flag = 1
    if flag == 0:
        row += 1
    else:
        row -= 1
for i in range(k):
    print("".join(enc[i]))
ct = ""
for i in range(k):
    for j in range(len(s)):
        if enc[i][j] != " ":
            ct+=enc[i][j]
print("CIPHER TEXT:", ct)


# RSA

p = int(input("Enter the value of p: "))
q = int(input("Enter the value of q: "))
n = p * q
print("N = " + str(n))
phi = (p-1) * (q-1)
print("Phi of N = " + str(phi))
e = int(input("Enter the value of public key: "))
should_continue = True
x = 1
while(should_continue):
    ans = ((x * phi ) + 1)
    if (ans % e == 0):
        should_continue = False
        d = ans / e
    else:
        x += 1
print("Value of Private Key (D) = " + str(d))
choice = int(input("Enter 1 for Encryption or 2 for Decryption: "))
if (choice == 1):
    pt = int(input("Enter the Value of Plain Text: "))
    ct = pt ** e % n
    print("CIPHER TEXT = " + str(ct))
else:
    ct = int(input("Enter the value of Cipher Text: "))
    pt = ct ** d % n
    print("PLAIN TEXT = " + str(pt))


# diffie hillman

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

# print(840//1176)