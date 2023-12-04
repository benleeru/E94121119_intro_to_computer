def fibonacci(n):  
    #n = int(input('Give an integer: '))
    fib_list=[]
    for i in range(n+1):
        if i==0 or i==1 :
            fib_list.append(i)
        else :
            ans = fib_list[i-1]+fib_list[i-2]
            fib_list.append(ans)        
    #print(fib_list[-1]) #0,1,1,2,3,5,8…費波納契數列首項算做第零項
    return fib_list[-1]

#伺服器端 樹莓派
import socket

def handle_client (client, client_addr):
       
    while True: 
        data_from_client = client.recv(1024).decode('utf-8')
        if not data_from_client: #在"客戶端"用ctrl+C關閉client端連線時
            break 
        
        print(f'Received from {client_addr}: {data_from_client}')
        result = fibonacci(int(data_from_client))
        print(f'Send to {client_addr}: {result}')
        message_to_client = str(result)
        client.send(message_to_client.encode())

    print(f'Connection with {client_addr} closed.')
    client.close()

while True:
    print('Waiting for connection…')#接著顯示"Waiting for connection…"
    BUF_SIZE=1024 #緩衝區
    server_addr=('192.168.137.98', 7000) #樹莓派的ip(IPV4), port
    server=socket.socket() #建立socket物件
    server.bind(server_addr) #將socket(套接字)綁定剛才指定的伺服器位址
    server.listen(5) #最大監聽數為5：伺服器一次只能連一個客戶端，5代表只允許伺服器被占用時，系統的最大連接數
    
    client, client_addr= server.accept() #TCP連線開線程，接受前端(我的電腦)連線的物件和位址，將這個返回的 socket 物件和位址信息分別賦值給變數 client 和 client_addr
    print (f'add connection from {client_addr}')
    
    handle_client (client, client_addr)