#! C:\Users\user\miniconda3\python.exe
from socket import *

SERVER = 'localhost'
# gethostname() '192.168.137.1'
# ipconfig >> You can use all of the IPv4 address 
# 'localhost'(127.0.0.1)
PORT = 12000
print('hostname: ', SERVER)
print('server: ', gethostbyname(SERVER))
clientSocket = socket(AF_INET, SOCK_STREAM)
clientSocket.connect((SERVER, PORT))

msg = input('input: ')

clientSocket.send(msg.encode())
msgu = clientSocket.recv(1024)
print('receive ', msgu.decode())

clientSocket.close()