text = input("Enter IP address in Binary Notation : ").split()[:4]
print("\nDecimal Notation for this IP is:")
for i in range(len(text)):
    if(i == 3):
        print(int(text[i], 2))
    else:
        print(int(text[i], 2), end = '.')