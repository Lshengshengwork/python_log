import socket

# 1. 创建一个socket
# 参数1： 指定协议 AF_INET  或 AF_INET6
# 参数2：  指定使用面向流的TCP协议
sk = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

# 2. 建立连接
# 参数： 是一个元祖，第一个元素为要连接的服务器的ip地址，第二个参数为端口
sk.connect(("www.baidu.com",80))

#
sk.send(b'GET / HTTP/1.1\r\nHost:www.baidu.com\r\nConnection: close\r\n\r\n')


# 等待接收数据
data = []

while True:
    # 每次接收1k的数据
    tempdata = sk.recv(1024)
    if tempdata:
        data.append(tempdata)
    else:
        break


dataStr = (b''.join(data).decode("utf-8"))
# 断开连接
sk.close()
print(dataStr)


# 把返回的hrader和html切一下，拆开
headers, HTML = dataStr.split('\r\n\r\n',1)
print(headers)
print(HTML)
