import socket 

serverport = 3000

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)  # SOCK_DGRAM for UDP 
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
s.bind(('',serverport))

max_size = 1024

while True:
    request, clientaddress = s.recvfrom(max_size)
    if(request == 'close'): break
    s.sendto(request, clientaddress)
    print len(request)

