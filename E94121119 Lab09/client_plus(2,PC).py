#coding=utf-8
#客戶端 我的電腦
import socket
 
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)# 建立客戶端(電腦端)的套接字socket
server_addr=('192.168.137.98', 7000) #遠端server(樹莓派)的ip, port
print(f'connect to {server_addr}')

client_socket.connect(server_addr) #連線

while True:
    give_server_something = input('give server something: ')# 向伺服器發送數據
    #give_server_something = 5

    if give_server_something.lower() == 'exit' :
        print ('connection closed')
        client_socket.close()
        break

    client_socket.send(give_server_something.encode('utf-8'))


#ssh E94121119@192.168.137.98
# python -u "server.py"
