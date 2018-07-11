# part--(c)

import socket 
serverport = 3000
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # SOCK_DGRAM for UDP , SOCK_STREAM for TCP
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
s.bind(('',serverport))
s.listen(5) #max 5 request at a time 

max_size = 40000


clientsocket, clientaddress = s.accept()

while True:
    request = clientsocket.recv(max_size)
    clientsocket.sendall(request)
    if (len(request)==0): break

clientsocket.close()













# count = 0
# calc= 0

# while (count!=10):
#     temp = base*(count+1)
#     request = clientsocket.recv(max_size)
#     print 'request: from client'
#     clientsocket.sendall(request)
#     leng = len(request)
#     print leng
#     if (temp == leng or calc==leng):
#         count += 1
#         calc=0
#     else:
#         calc += leng 
