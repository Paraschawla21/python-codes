text = input("Enter IP Adress in Decimal Notation : ")
print("IP Adress in Binary Notation for this is = " + ' ' .join(format(int(x), '08b') for x in text.split('.')))