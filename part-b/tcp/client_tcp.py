# part--(a)
# rtt for tcp of message size from 1byte to 1000bytes
import time
import socket 
print('request initiated: ')
serverip = "172.16.68.35"  # 127.0.0.1--localhost  #172.16.68.35 --remote ip
serverport = 3000

# INET shows that the tcp stream has a ipv4 address
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((serverip,serverport))
print("connected to server ")

max_size = 40000

msg_size = [1024,2048,3072,4096,5120,6144,7168,8192,9216,10240,11264,12288,13312,14336,
 15360,16384,17408,18432,19456,20480,21504,22528,23552,24576,25600,26624,27648,
 28672,29696,30720,31744,32768]

msg = []
for i in range(len(msg_size)-1,-1,-1):
    msg.append(bytearray(msg_size[i]))
    
diffarray = []

 

for i in range(len(msg)):
    ti = time.time()
    s.send(msg[i])
    response = s.recv(max_size)
    print len(response)
    tf = time.time()
    diffarray.append(format(tf-ti,'.6f'))

print diffarray
s.close()

throughputarray = []

for i in range(len(diffarray)):
    x = ( msg_size[31-i] * 2 ) / (float(diffarray[i])*1024*1024)
    throughputarray.append(x)

print throughputarray
f = open('data.txt','w')
f.write('Bytes : Throughput  \n')
for i in range(len(diffarray)):
    string = str(msg_size[i]) + ' : ' + str(throughputarray[31-i]) + ' \n'   
    f.write(string)

