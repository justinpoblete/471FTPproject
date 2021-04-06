import socket
import sys

serverName = sys.argv[1]
serverPort = int(sys.argv[2])
serverAddress = (serverName, serverPort)

clientSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
clientSocket.connect(serverAddress)

def lsCommand():
  #do something
def getCommand():
  #do something
def putCommand():
  #do something

while True:
  menu = {"ls": 2, "get": 3, "put": 4, "close": 5}
  commands = input("ftp>")
  commands = commands.split()

  if commands[0] in menu.keys():
    if menu[commands[0]] == 2:
      #do ls
      print("ls entered")
    elif menu[commands[0]] == 3:
      #do get
      print("get entered")
    elif menu[commands[0]] == 4:
      #do put
      print("put entered")
    elif menu[commands[0]] == 5:
      #close
      print("close entered")
      break
  else:
    print("Invalid command")
    break
