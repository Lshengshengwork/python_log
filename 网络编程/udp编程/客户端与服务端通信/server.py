import socket

udpServer = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

udpServer.bind(('192.168.2.123',8900))
print("upd服务启动.")
while True:
    data, addr = udpServer.recvfrom(1024)
    print("客户端{0}说：".format(addr),data.decode("utf-8"))