#coding:UTF-8
import socket

#创建一个socket对象
s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
host=socket.gethostname()
port=12345
#绑定要监听的端口
s.bind((host,port))
#开始监听，表示可以使用5个链接队列
s.listen(5)
while True:
	#等待链接，返回两个值，一个是链接，一个是客户端地址
	conn,addr=s.accept()  
	print("链接地址：",addr)
	#发送数据，python3只支持字节，因此转换成字节发送
	c.send("欢迎链接".encode('utf-8'))
	c.close()
