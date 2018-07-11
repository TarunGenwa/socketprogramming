# part--(c)

import time
import socket 
print('request initiated: ')
serverip = "172.16.68.35"  # 127.0.0.1--localhost  #172.16.68.35 --remote ip
serverport = 3000

# INET shows that the tcp stream has a ipv4 address
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((serverip,serverport))
print("connected to server ")

msg_size = [1024,2048,4096,8192,16384,32768]
# ,2048,4096,8192,16384,32768
max_size = 40000


diffarray = []
sumx=0
for i in range(len(msg_size)):
    msg = bytearray(1024*1024)
    t = msg_size[i]
    print t
    print len(msg)
    sumx = 0
    ti = time.time()
    while msg:
        s.send(msg[:t])
        msg = msg[t:]
        response = s.recv(max_size)
        sumx += len(response)        
        print sumx
    tf = time.time()
    diffarray.append(format(tf-ti,'.6f'))
s.close()
print diffarray

throughputarray = []
for i in range(len(diffarray)):
    x = ( 2 ) / (float(diffarray[i]))
    throughputarray.append(x)

print throughputarray

f = open('data.txt','w')
f.write('Bytes : Throughput  \n')
for i in range(len(diffarray)):
    string = str(msg_size[i]) + ' : ' + str(throughputarray[i]) + ' \n'   
    f.write(string)




# def sendall_data (sock, data, flags=0):
#     ret = sock.send(data,flags)
#     if ret>0:
#         print ret
#         return sendall_data(sock,data[ret:],flags)
#     else:
#         return None
# diffarray = []

# arr = []

# for i in range(len(msg_size)):
#     ti = time.time()
#     x = s.send(msg_size[i])
#     arr.append(x) 
#     sumx  = 0
#     count=0
#     while (sumx!=len(msg)):
#         count += 1
#         response = s.recv(max_size)
#         sumx += len(response)
#         print sumx 
#     print count    
#     tf = time.time()
#     diffarray.append(format(tf-ti,'.6f'))

# print arr
# print diffarray
# s.close()

# f = open('data.txt','w')
# for i in range(len(diffarray)):
#     x = 1024*(i+1)

#     f.write(str(x)+ ':' + str(diffarray[i]) + '\n' )


