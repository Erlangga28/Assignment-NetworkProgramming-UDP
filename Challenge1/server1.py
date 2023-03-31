import socket
import random 
import sys
import os

server_address = ('127.0.0.1', 5000)
server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
server_socket.bind(server_address) 

filenamestart = 'receivedfile_'
filecount = 0
     
try:
    while True:
        filecount += 1
        filename = filenamestart + str(filecount) + '.txt'
        while True:
            data, client_address = server_socket.recvfrom(1024)
            if data:
                break
        actual_filesize = int(data.decode())
        print(str(actual_filesize))
        with open(filename, 'wb') as f:
            while True:
                try:
                    server_socket.settimeout(3)
                    data = server_socket.recv(1024)
                    if not data:
                        break
                except socket.timeout:
                    break
                else:
                    f.write(data)
             
        print('finished')   
        received_filesize = int(os.path.getsize(filename))
        print (str(received_filesize))
        percentage = (received_filesize / actual_filesize) * 100
        print('')
        print('Finished receiving from ' + str(client_address) + ' from socket ' + str(server_socket.getsockname()))
        print('received ' + str(percentage) + '%% of the file from sender.')
        server_socket.sendto(str(percentage).encode(), client_address)
        
        
        if KeyboardInterrupt:
            break

except KeyboardInterrupt:
    print('Server is interrupted')