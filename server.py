import socket 
import threading 


port = 8080 #Runs on port 8080
hoster = "192.168.1.58" #Hoster's Local Address
addr = (hoster, port)
activeconnection = True

host = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #Creates an socket object
host.bind(addr)

# Main

def client(connection, addr):
    print(f"Connection {addr}")

    while activeconnection:
        message = connection.recv(2048)


    

def starts():
    host.listen() #lisents in on incoming connections
    while True:
        connection, addr = host.accept() #accepts the connections
        thread = threading.Thread(tar=client, args=(connection, addr))
        thread.start()
        print(f"Connections: {threading.activeCount() - 1}")



print("Starting")
starts()



