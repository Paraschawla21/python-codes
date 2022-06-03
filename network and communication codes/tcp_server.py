import socket
s = socket.socket()    # by default it will be tcp and ipv4
print("SOCKET CREATED")
s.bind(("localhost", 8474))
s.listen(3)
print("Waiting for the connection")
while True:
    c, add = s.accept()
    name = c.recv(1024).decode()
    print("Connected with ", add, name)
    c.send(bytes("Welcome to Socket Programming with TCP", "utf-8"))
    c.close()