import socket

h = "127.0.0.1" #Host address
p = 65432 #port to listen on

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((h, p))
    s.listen()
    connection, address = s.accept()
    with connection:
        print(f"Connected by {address}")
        while True:
            data = connection.recv(1024)
            if not data: 
                break
            connection.sendall(data) #Any data recieved from the client is echoed back to the server using server