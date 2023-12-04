#coding=utf-8
#客戶端 raspberryPI
import socket

import threading

def input_thread(client_socket):
    while True:
        give_server_something = input('give server something: ')
        if give_server_something.lower() == 'exit':
            print('connection closed')
            client_socket.close()
            break
        client_socket.send(give_server_something.encode('utf-8'))

# 在主線程中連接伺服器
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_addr = ('192.168.137.98', 7000)
print(f'connect to {server_addr}')
client_socket.connect(server_addr)

# 啟動一個新線程處理用戶輸入
threading.Thread(target=input_thread, args=(client_socket,)).start()

# 主線程可以處理其他事情，如接收伺服器的數據
while True:
    data = client_socket.recv(1024)
    if not data:
        print('connection closed by server')
        break
    print('received:', data.decode('utf-8'))
