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