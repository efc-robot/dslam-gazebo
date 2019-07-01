#!/usr/bin/env python
# -*- coding: utf-8 -*-

'a server example which send hello to client.'

import time, socket, threading

def tcplink(sock, addr):
    print ('Accept new connection from %s:%s...' % addr)
    sock.send('Welcome!'.encode('utf-8'))
    while True:
        data = sock.recv(1024)
        data = data.decode('utf-8')
        if data == 'exit' or not data:
            break
        elif data == 'u':
            sock.send('u'.encode('utf-8'))
        elif data == 'i':
            sock.send('i'.encode('utf-8'))
        elif data == 'o':
            sock.send('o'.encode('utf-8'))
        elif data == 'j':
            sock.send('j'.encode('utf-8'))
        elif data == 'k':
            sock.send('k'.encode('utf-8'))
        elif data == 'l':
            sock.send('l'.encode('utf-8'))
        elif data == 'm':
            sock.send('m'.encode('utf-8'))
        elif data == ',':
            sock.send(','.encode('utf-8'))
        elif data == '.':
            sock.send('.'.encode('utf-8'))
        elif data == 'q':
            sock.send('q'.encode('utf-8'))
        elif data == 'z':
            sock.send('z'.encode('utf-8'))
        elif data == 'w':
            sock.send('w'.encode('utf-8'))
        elif data == 'x':
            sock.send('x'.encode('utf-8'))
        elif data == 'e':
            sock.send('e'.encode('utf-8'))
        elif data == 'c':
            sock.send('c'.encode('utf-8'))
        elif data == 'k':
            sock.send('k'.encode('utf-8'))
        elif data == ' ':
            sock.send(' '.encode('utf-8'))
    sock.close()
    print ('Connection from %s:%s closed.' % addr)

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# 监听端口:
s.bind(('192.168.31.235', 50007))
s.listen(10)
print ('Waiting for connection...')
while True:
    # 接受一个新连接:
    sock, addr = s.accept()
    # 创建新线程来处理TCP连接:
    t = threading.Thread(target=tcplink, args=(sock, addr))
    t.start()
