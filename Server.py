import socket
import time

SERVER_PORT = 12000

server_socket = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
server_socket.bind(("127.0.0.1",SERVER_PORT))

print("Server ready to receive")

while 1:

    message,client_adress = server_socket.recvfrom(2048)

    current_time = time.localtime()
    final_time = time.strftime("%H:%M:%S", current_time)

    message = final_time + '#' + message
    
    pacote = message.split('#')

    print("Current_Time: {}".format(pacote[0]))
    print("Client_name: {}".format(pacote[1]))
    print("Message from Client:{}".format(pacote[2]))
    print("Client IP Address:{}".format(client_adress))

    server_socket.sendto(pacote[0] + '#' + pacote[1] + '#' + pacote[2] ,client_adress)
    