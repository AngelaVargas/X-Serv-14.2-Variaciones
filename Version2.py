 
import socket

# Create a TCP objet socket and bind it to a port
# We bind to 'localhost', therefore only accepts connections from the
# same machine
# Port should be 80, but since it needs root privileges,
# let's use one above 1024

mySocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
mySocket.bind(('localhost', 1234))

# Queue a maximum of 5 TCP connection requests

mySocket.listen(5)

# Accept connections, read incoming data, and answer back an HTML page
#  (in an infinite loop)

while True:
    print ('Waiting for connections')
    (recvSocket, address) = mySocket.accept()
    print ('HTTP request received:')
    print (recvSocket.recv(1024))
    recvSocket.send(bytes("HTTP/1.1 200 OK\r\n\r\n" +
							"<html><body><h1>Redirigiendo...</h1>" +
							"<META HTTP-EQUIV='REFRESH' CONTENT='1;URL=http://gsyc.es/'>" +
							"</body></html>" +
							"\r\n", 'utf-8'))
    recvSocket.close()
