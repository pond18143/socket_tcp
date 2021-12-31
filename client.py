from socket import *

serverName = '192.168.1.37' #destination
# serverName = 'localhost' #destination
serverPort = 13000
clientSocket = socket(AF_INET, SOCK_STREAM) #create socket for send to server
clientSocket.connect((serverName,serverPort)) #connect and wait for handshake
sentence = input('Input lowercase sentence: ')
clientSocket.send(sentence.encode()) #send message encode
modifiedSentence = clientSocket.recv(1024) #read reply form socket to string not have servername port
print ('From Server: ', modifiedSentence.decode())
clientSocket.close() #close