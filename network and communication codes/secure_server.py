import socket
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


s = socket.socket()
#s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print("Socket created")
s.bind(('localhost', 9999))

s.listen(3)
print("waiting for connection: ")

while True:
    c, addr = s.accept()
    name = c.recv(1024).decode()
    print("connected with", addr, name)

    c.send(bytes('welcome', 'utf-8'))

    list4 = name.split(',')
    # print(list4)

    for i in range(0, len(list4)):
        list4[i] = int(list4[i])

    # print(list4)

    list5 = []
    for i in range(0, len(list4)):
        plain_text = list4[i]**D % N
        list5.append(plain_text)
    # print("decrypted",list5)

    str = " "
    for i in range(0, len(list5)):
        str = str+chr(list5[i])

    print("Original message:", str)

    c.close()