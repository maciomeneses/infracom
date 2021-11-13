import socket

SERVER_NAME = '127.0.0.1'
SERVER_PORT = 12000

is_running = False

while 1:

    print('Bem vindo, cliente!')
    print('Conectar a sala digite: hi, meu nome eh <nome_de_usuario>')
    print('Sair da sala digite: bye')
    print('Exibir lista de usuarios digite: list')

    comando = raw_input()
    if comando[0:16] == 'hi, meu nome eh ':
        client_Socket = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
        Client_name = comando[16:]
        is_running = True
        print('Ola!')
        print('Digite suas mensagens e aperte ENTER para enviar!')

    while is_running:

        message = raw_input()

        client_Socket.sendto(Client_name + '#' + message ,(SERVER_NAME,SERVER_PORT))

        if message == 'bye':
            is_running = False
            client_Socket.close()
            break

        message_from_server, server_adress = client_Socket.recvfrom(2048)

        pacote = message_from_server.split('#')

        print(pacote[0] + ' ' + pacote[1] + ': ' + pacote[2])
