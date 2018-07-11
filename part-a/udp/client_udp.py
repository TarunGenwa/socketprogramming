import socket 
import time
print('client request initiated')

serverip = "172.16.68.35"  # 127.0.0.1--localhost  #172.16.68.35 --remote ip
serverport = 3000

# INET shows that the tcp stream has a ipv4 address
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

max_size = 1024
array = [1,100,200,300,400,500,600,700,800,900,1000]

msg = []
for i in range(len(array)-1,-1,-1):
    msg.append(bytearray(array[i]))

msg.append('close')

diffarray = []

for i in msg:
    if(i == 'close'):
        s.sendto(i,(serverip,serverport))
        break
    ti = time.time()
    s.sendto(i,(serverip,serverport))
    response, addr = s.recvfrom(max_size)
    print len(response)
    tf = time.time()
    diffarray.append(format(tf-ti,'.6f'))


print diffarray
s.close()

f = open('data.txt','w')
f.write('Rtt : Bytes \n')
for i in range(len(diffarray)):
    string = str(diffarray[10-i]) + ' : ' + str(array[i]) + ' \n'   
    f.write(string)
