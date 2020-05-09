#! C:\Users\user\miniconda3\python.exe
from socket import *

PORT = 12000
serverSocket = socket(AF_INET, SOCK_STREAM)
serverSocket.bind(('', PORT))
serverSocket.listen(1)

print('The server is ready to receive.')

canLoop = True

while canLoop:
    connSocket, addr = serverSocket.accept()
    msg = connSocket.recv(1024).decode()
    if(msg == 'bye'):
        canLoop = False
        serverSocket.close()
    msgu = msg.upper()
    connSocket.send(msgu.encode())
    print('send ', msgu, 'to ', addr)
    connSocket.close()