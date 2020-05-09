#! C:\Users\user\miniconda3\python.exe
from socket import *

PORT = 12000
serverSocket = socket(AF_INET, SOCK_DGRAM)
serverSocket.bind(('', PORT))

print('The server is ready to receive.')

canLoop = True

while canLoop:
    msg, addr = serverSocket.recvfrom(2048)
    msgu = msg.decode().upper()
    serverSocket.sendto(msgu.encode(), addr)
    print('send ', msgu, 'to ', addr)
    if(msg.decode() == 'bye'):
        canLoop = False
        serverSocket.close()