import socket
import sys
 
# Create a TCP/IP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
 
# Define host
host = '127.0.0.1'
 
# define the communication port
port = 12345
 
# Bind the socket to the port
sock.bind((host, port))
# Listen for incoming connections
sock.listen(1)
 
# Wait for a connection
print ('waiting for a connection')
connection, client = sock.accept()
 
print (client, 'connected')
 
# Receive the data in small chunks and retransmit it
data1 = connection.recv(16)
data2 = connection.recv(16)


print ('number 1 received "%s"' % data1)
print ('number 2 received "%s"' % data2)
num1 = list(map(int, data1.split()))
num2 = list(map(int, data2.split()))

data3 = num1[0]*num2[0]
print (data3)
connection.close()