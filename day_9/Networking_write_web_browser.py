import socket
#lv an HTTP request in python
mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
mysock.connect(('data.pr4e.org', 80))
cmd = 'GET http://data.pr4e.org/romeo.txt HTTP/1.0\r\n\r\n'.encode()
mysock.send(cmd)

while True:
    data = mysock.recv(512)
    if len(data) < 1:
        break
    print(data.decode())
mysock.close()

#test QA
'''
cmd = 'GET http://www.ribison.com/ HTTP/1.0\r\n\r\n'.encode()
mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
mysock.connect(('www.ribison.com', 80))
mysock.send(cmd)

while True:
    data = mysock.recv(512)
    if len(data) < 1:
        break
    print(data.decode(),end='')
mysock.close()
'''