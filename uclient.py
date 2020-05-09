#! C:\Users\user\miniconda3\python.exe
from socket import *

SERVER = '127.0.0.1' #'localhost'
PORT = 12000

clientSocket = socket(AF_INET, SOCK_DGRAM)
msg = input('input: ')
clientSocket.sendto(msg.encode(), (SERVER, PORT))

msgu, addr = clientSocket.recvfrom(2048)
print('receive ', msgu.decode(), 'from ', addr)

clientSocket.close()