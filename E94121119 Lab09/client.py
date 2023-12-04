#客戶端 我的電腦
import socket
 
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)# 建立客戶端(電腦端)的套接字socket
server_addr=('192.168.137.98', 7000) #遠端server(樹莓派)的ip, port
print(f'connect to {server_addr}')
#server=socket.socket() #建立socket物件
client_socket.connect(server_addr) #連線

while True:
    n_for_fibonacci = input('the fabonnaci(n) when n = ')# 向伺服器發送數據

    if n_for_fibonacci.lower() == 'exit': 
        print ('connection closed')
        break

    client_socket.send(n_for_fibonacci.encode('utf-8'))

    # 接收從伺服器發送的數據
    received_data = client_socket.recv(1024).decode('utf-8') #python docs 搜尋'socekt.recv'
    print(f"the ans receive from server is {received_data}") 


#ssh E94121119@192.168.137.98
# python -u "server.py"
