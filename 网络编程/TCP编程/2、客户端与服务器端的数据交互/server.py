import socket

# 创建一个socket
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# 绑定ip 端口
server.bind(('192.168.2.123',8080))
# 监听
server.listen(5)
print("服务器启动成功...")
# 等待链接
clientSocket, clientAddress = server.accept()
print("%s -- %s 链接成功"%(str(clientSocket),clientAddress))
while True:
    data = clientSocket.recv(1024)
    print("客户端说："+ data.decode("utf-8"))
    clientSocket.send("来了，老弟".encode("utf-8"))