# -*- coding: utf-8 -*-
import socket
import threading


# create a socket and assign an address and a port to the server
bind_ip = "0.0.0.0"
bind_port = 9999
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((bind_ip, bind_port))
server.listen(5)  # sets the max number of connections (chat members) to 5

print "[*] Chat created at %s:%d" % (bind_ip, bind_port)

def handle_client(client_socket):
  client_socket.send("Introduce yourself: ")
  nickname = client_socket.recv(1024)[0:-1]
  print "[*] %s %s" % (nickname, "has joined the chat")

  while True:
    request = client_socket.recv(1024)[0:-1]
    if len(request) == 0:
      print "[*] %s %s" % (nickname, "has left the chat")
      client_socket.close()
      break
    print "%s> %s" % (nickname, request)


while True:
  client, addr = server.accept()
  # create a thread for a client
  client_handler = threading.Thread(target=handle_client, args=(client,))
  client_handler.start()
