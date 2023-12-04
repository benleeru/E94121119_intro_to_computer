#coding=utf-8
#server raspberryPI    
import socket
import threading

def handle_client (client, client_addr):

    while True: 
        
        data_from_client = client.recv(1024).decode('utf-8')
        
        if not data_from_client: #When the client closes the connection using Ctrl+C.
            break 
        
        print(f'Add connection from {client_addr}: {data_from_client}')

    print(f'Connection with {client_addr} closed.')
    client.close()

print('Waiting for connection')
BUF_SIZE=1024 #buffer zone
server_addr=('192.168.137.98', 7000) 
server=socket.socket() #Create a socket object.
server.bind(server_addr) #Bind the socket to the previously specified server address.
server.listen(5) #Maximum listening backlog is 5
while True: #Client connection.
    client, client_addr= server.accept() 
    print (f'Add connection from {client_addr}')
    
    new_client = threading.Thread(target=handle_client, args=(client,client_addr ))
    
    new_client.start()    
    
    #client_handler : a 'variable' to store the created thread object.
    #threading.Thread :creates a new thread, and the handle_client function runs in that thread.
    #threading.Thread Create a new thread, and execute the handle_client function within the thread.