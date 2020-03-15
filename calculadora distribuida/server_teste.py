import socket 

serverPort = 8081
serverName = 'localhost'
mensagem = 0

serverSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
serverSocket.bind((serverName, serverPort)) 
serverSocket.listen(5)

print('Conectado com: %s, %d'%(serverName, serverPort))

def recebido_cliente(connectionSocket):
    mensagem = connectionSocket.recv(1024).decode()
    return mensagem

def enviando_cliente(resultado):
    connectionSocket.send(resultado.encode())
    connectionSocket.close()


while True:
    connectionSocket, clientAddress = serverSocket.accept()

    resultado1 = recebido_cliente(connectionSocket)

    if(resultado1[1] == '+'):
        resultado = int(resultado1[0])+int(resultado1[2])
    elif(resultado1[1] == '-'):
        resultado = int(resultado1[0])-int(resultado1[2])
    elif(resultado1[1] == '*'):
        resultado = int(resultado1[0])*int(resultado1[2])
    elif(resultado1[1] == '/'):
        resultado = int(resultado1[0])/int(resultado1[2])
    else: print("conta inválida")
    
    enviando_cliente(str(resultado))


