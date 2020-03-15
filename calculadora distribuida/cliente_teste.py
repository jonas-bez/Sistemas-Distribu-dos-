import socket 

serverName = 'localhost'
serverPort = 8081
messagem = "dentro"

while True:	
	clientSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	clientSocket.connect((serverName, serverPort))

	conta=""
	conta += input('Digite uma número: ')
	conta += input('Digite operando: ')
	conta += input('Digite uma número: ')

	clientSocket.send(conta.encode())
	
	modifiedMessage, serverAddress = clientSocket.recvfrom(2048)
	rsultado = modifiedMessage.decode()
	print('RESPOSTA: ', rsultado)
	clientSocket.close()
