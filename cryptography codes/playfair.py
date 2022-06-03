#play fair cipher
key = input("Enter key: ")
key = key.replace(" ", "")
key = key.upper()
my_matrix = [[" " for i in range(5)] for j in range(5)]
result = []
for c in key:
    if c not in result:
        if c == 'J':
            result.append('I')
        else:
            result.append(c)
flag = 0
for i in range(65, 91):
    if chr(i) not in result:
        if chr(i) == "I" and chr(74) not in result:
            result.append("I")
            flag = 1
        elif flag == 0 and i == 73 or i == 74:
            pass
        else:
            result.append(chr(i))
k = 0
for i in range(0, 5):
    for j in range(0, 5):
        my_matrix[i][j] = result[k]
        k += 1
print(my_matrix)