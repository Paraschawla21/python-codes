import socket
print("Enter a message: ")
text = input()
textlength = len(text)
list = []
for char in text:
    ascii = ord(char)
    list.append(ascii)

# print(list)

P = 17
Q = 7

fi_n = (P-1)*(Q-1)

i = 1
while(i > 0):
    if(fi_n % i != 0):
        E = i
        #print("the value for E is:",E)
        break
    else:
        i = i+1

j = 1
while(j > 0):
    temp1 = (j*fi_n+1)/E
    temp2 = int(temp1)
    temp3 = temp1-temp2
    if(temp3 == 0.0):
        if(temp2*E % fi_n == 1):
            D = temp2
            #print("The value for D is:",D)
            break
        else:
            j = j+1
    else:
        j = j+1


N = P*Q
list2 = []
for i in range(0, len(list)):
    cipher_text = list[i]**E % N
    list2.append(cipher_text)

# print("encrypted",list2)

#***********#

c = socket.socket()
#c=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# 172.16.33.151
c.connect(('localhost', 9999))
#name=input("enter ur name: ")
name = ",".join([str(i) for i in list2])

c.send(bytes(name, 'utf-8'))

print(c.recv(1024).decode())
