import socket
import sys

serverName = socket.gethostbyname(socket.gethostname())
serverPort = int(sys.argv[1])
serverAddress = (serverName, serverPort)
print(socket.gethostname())

serverSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
serverSocket.bind(serverAddress)
serverSocket.listen(5)

while True:
  clientSocket, address = serverSocket.accept()
  print(f"Connection from {address} has been established.")
  clientSocket.send(bytes("Hey there!!!", "utf-8"))
  clientSocket.close()
