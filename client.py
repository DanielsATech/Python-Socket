import socket

h = "127.0.0.1"
p = 65432

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((h, p))
    s.sendall("Data Recieved")
    data = s.recv(1024)

print(f"recieved {data!r}")