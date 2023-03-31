import socket 
import sys
import os

server_address = ('127.0.0.1', 5000)
client_socket = socket. socket(socket.AF_INET, socket.SOCK_DGRAM)
client_socket.connect(server_address) 

buf = 1024
filename = str(input('Input filename to be send: '))

try:
    filesize = int(os.path.getsize(filename))
    client_socket.send(str(filesize).encode())
    with open(filename, 'rb') as f:
        while True:
            data = f.read(1024)
            if not data:
                break
            client_socket.send(data)
        
    while True:
        try:
            percentage = float(client_socket.recv(1024).decode())
            print('Server received ' + str(percentage) + '%% of the file')
        except socket.timeout:
            print ('Server is down') 
        else:
            break
        
except KeyboardInterrupt:
    print('Keyboard interrupt')