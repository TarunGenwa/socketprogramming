# part--(b) 

import socket 
serverport = 3000
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # SOCK_DGRAM for UDP , SOCK_STREAM for TCP
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
s.bind(('',serverport))
s.listen(5) #max 5 request at a time 

clientsocket, clientaddress = s.accept()

max_size = 40000

while True:
    request = clientsocket.recv(max_size)
    if (len(request)==0): break
    clientsocket.sendall(request)
    print len(request)

clientsocket.close()