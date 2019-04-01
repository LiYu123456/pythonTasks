#coding=UTF-8
import socket

#创建一个socket对象
s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
host=socket.gethostname()
port=12345
#链接到服务端
s.connect((host,port))
#接收数据,并制定大小1024
data=s.recv(1024)
#解码显示
print(data.decode())
s.close()