import socket
#lv representing   string with ord()
#http://unicode.org/charts/
print(ord('H'))
print(ord('e'))
print(ord('\n'))


#lv1 encode() > send() > recv() > decode() work of socket
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
which type of encoding do most websites use?
UTF-8
'''