from socket import *

serverPort = 13000
serverSocket = socket(AF_INET,SOCK_STREAM) #create tcp socket
serverSocket.bind(('',serverPort)) #define basic for connect
serverSocket.listen(1) #listen incoming request
print ('The server is ready to receive')
while True:
    connectionSocket, addr = serverSocket.accept() #server wait on accept and difine new socket for return
    sentence = connectionSocket.recv(1024).decode() #read bytes from socket not define address as in udp
    capitalizedSentence = sentence.upper() #upper
    print(sentence)
    connectionSocket.send(capitalizedSentence.encode()) #encode and send to client
    connectionSocket.close()